from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from classroom.models import class_room, Comment, Classworks, Headings, SubHeadings, Enrolled, EnrolledTeacher
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.urls import reverse_lazy
from classroom.forms import CommentForm, ClassworksForm, EnrollForm, TeacherEnrollForm
from .models import User, Profile
from .decorators import allowed_users, class_enrolled
from .filters import ProfileFilter
from .mixins import CreatorAccessMixin, SuperUserAccessMixin
from cuser.middleware import CuserMiddleware
from itertools import chain

# Create your views here.

class signup(CreateView):
    form_class=SignUpForm
    template_name= 'registration/signup.html'
    success_url= reverse_lazy('account:login')

class ClassesList(LoginRequiredMixin, ListView):
        queryset= class_room.objects.all()
        template_name="registration/home.html"
        def get_queryset(self):
            if self.request.user.is_superuser:
                return class_room.objects.all()
            else:
                class1=class_room.objects.filter(creator=self.request.user)
                class2=class_room.objects.filter(teachers=self.request.user)
                class3=class_room.objects.filter(students=self.request.user)
                class4=chain(class1,class2,class3)
                return class4

class EnrollClass(LoginRequiredMixin, CreateView):
    model=Enrolled
    fields=["classroom",]
    template_name='registration/joinclass.html'
    success_url= reverse_lazy('account:home')

#    def save(self, *args, **kwargs):
#        self.student_profile = CuserMiddleware.get_user()
#        super(Enrolled,self).save(*args, **kwargs)

    def form_valid(self, form):
        form.instance.student_profile = self.request.user
        return super(EnrollClass, self).form_valid(form)

class StudentEnrollClass(LoginRequiredMixin, CreateView):
    model=Enrolled
    fields=["student_profile", "date"]
    template_name='registration/studentjoinclass.html'
    success_url= reverse_lazy('account:home')



    def form_valid(self,form):
        form.instance.classroom = classroom
        return super(StudentEnrollClass, self).form_valid(form)

class TeacherEnrollClass(LoginRequiredMixin, CreateView):
    model=EnrolledTeacher
    fields=["teacher_profile", "date"]
    template_name='registration/teacherjoinclass.html'
    success_url= reverse_lazy('account:home')


    def form_valid(self, form):
    #    classroom= get_object_or_404(class_room)
        form.instance.classroom = classroom
        return super(TeacherEnrollClass, self).form_valid(form)



class ClassesCreate(LoginRequiredMixin, CreateView):
    model=class_room
    fields=["Name", "class_number", "slug", "section", "room", "subject", "startdate", "status",]
    template_name="registration/classes-create-update.html"
class ClassesUpdate(LoginRequiredMixin,CreatorAccessMixin, UpdateView):
    model=class_room
    fields=["Name", "class_number", "section", "room", "subject", "startdate", "status",]
    template_name = "registration/classes-create-update.html"
    success_url= reverse_lazy('account:home')
class ClassesDelete(LoginRequiredMixin,CreatorAccessMixin, DeleteView):
    model=class_room
    template_name = "registration/classes_confirm_delete.html"
    success_url= reverse_lazy('account:home')


class EnrollList(LoginRequiredMixin, ListView):
        queryset= Enrolled.objects.all()
        template_name="registration/classroom.html"



@login_required(login_url='account:login')
@class_enrolled
def class_comment(request, slug):
    #creates view for comments inside the classroom.
    template_name = 'registration/classcomment.html'
    post = get_object_or_404(class_room, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,})
@login_required(login_url='account:login')
@class_enrolled
def class_classwork(request,slug):
    template_name = 'registration/classworks.html'
    classworks_post=get_object_or_404(class_room, slug=slug)
    class_works = classworks_post.classworks.filter(classworks_active=True)
    new_classworks = None
    # Comment posted
    if request.method == 'POST':
        classworks_form = ClassworksForm(data=request.POST)
        if classworks_form.is_valid():

            # Create Comment object but don't save to database yet
            new_classworks = classworks_form.save(commit=False)
            # Assign the current post to the comment
            new_classworks.classworks_post = classworks_post
            # Save the comment to the database
            new_classworks.save()
    else:
        classworks_form = ClassworksForm()
    return render(request, template_name, {'classworks_post': classworks_post,
                                           'class_works': class_works,
                                           'new_classworks': new_classworks,
                                           'classworks_form': classworks_form,})

@login_required(login_url='account:login')
@class_enrolled
def class_student(request, slug):
    template_name = 'registration/classstudent.html'
    classroom = get_object_or_404(class_room, slug=slug)
    students = classroom.classroom_enroll.all()
    new_student = None
    if request.method == 'POST':
        def form_valid(self, form):
            form.instance.classroom = classroom
            return super(class_student, self).form_valid(form)
        enroll_form = EnrollForm(data=request.POST)
        if enroll_form.is_valid():

            # Create Comment object but don't save to database yet
            new_student = enroll_form.save(commit=False)
            # Assign the current post to the comment
            new_student.classroom = classroom
            # Save the comment to the database
            new_student.save()
    else:
        enroll_form = EnrollForm()
    return render(request, template_name, {'students': students,
                                           'classroom': classroom,
                                           'new_student': new_student,
                                           'enroll_form': enroll_form,})

@login_required(login_url='account:login')
@class_enrolled
def class_teacher(request, slug):
    template_name = 'registration/classteacher.html'
    teacherclassroom = get_object_or_404(class_room, slug=slug)
    teachers= teacherclassroom.classroom_enrollteacher.all()
    new_teacher= None
    if request.method == 'POST':
        def form_valid(self, form):
            form.instance.tclassroom = teacherclassroom
            return super(class_teacher, self).form_valid(form)
        teacherenroll_form = TeacherEnrollForm(data=request.POST)
        if teacherenroll_form.is_valid():

            # Create Comment object but don't save to database yet
            new_teacher = teacherenroll_form.save(commit=False)
            # Assign the current post to the comment
            new_teacher.teacherclassroom = teacherclassroom
            # Save the comment to the database
            new_teacher.save()
    else:
        teacherenroll_form = TeacherEnrollForm()
    return render(request, template_name, {'teachers': teachers,
                                           'teacherclassroom': teacherclassroom,
                                           'new_teacher': new_teacher,
                                           'teacherenroll_form': teacherenroll_form,})






class HeadingsList(LoginRequiredMixin, ListView):
        queryset= Headings.objects.all()
        template_name="registration/classroom.html"
        def get_queryset(self):
            if self.request.user.is_superuser:
                return Headings.objects.all()
            else:
                return Headings.objects.filter(class_room=self.request.user)


class SubheadingsList(LoginRequiredMixin, ListView):
        queryset= SubHeadings.objects.all()
        template_name="registration/classroom.html"
        def get_queryset(self):
            if self.request.user.is_superuser:
                return SubHeadings.objects.all()
            else:
                return SubHeadings.objects.filter(User=self.request.user)
