
from django.db import models
from django.utils import timezone
from extensions.utils import jalali_converter
from django.urls import reverse
from account.models import User, Profile
from .managers import  EnrolledManager
from cuser.middleware import CuserMiddleware


# Create your models here.

class class_room(models.Model):
    STATUS_CHOICES=(
        ('public','عمومی'),
        ('private','خصوصی'),
    )

    Name=models.CharField(max_length=200, verbose_name ="نام کلاس")
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='class_creator', verbose_name="ایجادکننده کلاس")
    class_number=models.SlugField(unique=True,verbose_name ="شماره کلاس")
    slug=models.SlugField(max_length=100,unique=True, verbose_name ="آدرس کلاس")
    section=models.CharField(max_length=200, verbose_name ="بخش")
    room=models.CharField(max_length=200, verbose_name ="اتاق")
    subject=models.CharField(max_length=200, verbose_name ="موضوع")
    startdate=models.DateTimeField(default=timezone.now, verbose_name ="تاریخ شروع کلاس")
    created_time=models.DateTimeField(auto_now_add=True, verbose_name ="تاریخ ایجاد")
    finished_time=models.DateTimeField(default=timezone.now, verbose_name ="تاریخ پایان کلاس")
    updated_time=models.DateTimeField(auto_now=True, verbose_name ="تاریخ آخرین آپدیت")
    status=models.CharField(max_length=7, choices=STATUS_CHOICES, verbose_name ="وضعیت انتشار")
    students=models.ManyToManyField(User, through='Enrolled', related_name='classstudents')
    teachers=models.ManyToManyField(User, through='EnrolledTeacher', related_name='classteachers')
#    teacher_members=models.ManyToManyField(User, blank=False, limit_choices_to={'role': 2}, related_name='teachers', verbose_name="لیست اساتید")


    class Meta:
        verbose_name = "کلاس"
        verbose_name_plural = "کلاس‌ها"

    def __str__(self):
        return self.Name

    def get_absolute_url(self):
        return reverse("account:home")

    def jcreated_time(self):
        return jalali_converter(self.created_time)

    def jstartdate(self):
        return jalali_converter(self.startdate)

    def save(self, *args, **kwargs):
        self.creator = CuserMiddleware.get_user()
        super(class_room,self).save(*args, **kwargs)




class Comment(models.Model):
    post = models.ForeignKey(class_room,null=False, on_delete=models.CASCADE,related_name='comments',verbose_name ="نام کلاس")
    name = models.CharField(null=True,verbose_name ="نام", max_length=80)
    body = models.TextField(null=True,verbose_name ="متن")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='comment_creator', verbose_name="نام نظر‌دهنده")

    class Meta:
        ordering = ['created_on']
        verbose_name = "گفتگو"
        verbose_name_plural = "گفتگوها"
    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    def jcreated_on(self):
        return jalali_converter(self.created_on)
    def approve(self):
        self.approved_comment = True
        self.save()
    def save(self, *args, **kwargs):
        self.creator = CuserMiddleware.get_user()
        super(Comment,self).save(*args, **kwargs)


class Classworks(models.Model):
    classworks_post = models.ForeignKey(class_room,null=False, on_delete=models.CASCADE,related_name='classworks',verbose_name ="نام کلاس")
    classworks_name = models.CharField(null=True,verbose_name ="نام مبحث", max_length=80)
    classworks_body = models.TextField(null=True,verbose_name ="متن")
    classworks_created_on = models.DateTimeField(auto_now_add=True)
    classworks_active = models.BooleanField(default=True)
    creator = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='classwork_creator', verbose_name="نام استاد")

    class Meta:
        ordering = ['classworks_created_on']
        verbose_name = "تکلیف"
        verbose_name_plural = "تکالیف"
    def __str__(self):
        return 'Classwork {} by {}'.format(self.classworks_body, self.classworks_name)
    def classworks_jcreated_on(self):
        return jalali_converter(self.classworks_created_on)
    def approve(self):
        self.approved_comment = True
        self.save()
    def save(self, *args, **kwargs):
        self.creator = CuserMiddleware.get_user()
        super(Classworks,self).save(*args, **kwargs)


class Headings(models.Model):
    headingsـpost= models.ForeignKey(class_room,null=False, on_delete=models.CASCADE, related_name='headings',verbose_name="کلاس")
    headings_name= models.CharField(null=True,verbose_name="عنوان", max_length=200)

    class Meta:
        verbose_name= "عناوین"
        verbose_name_plural = "عناوین"
    def __str__(self):
        return self.headings_name


class SubHeadings(models.Model):
    subheadings_post= models.ForeignKey(Headings,null=False, on_delete=models.CASCADE, related_name='subheadings',verbose_name="عنوان")
    subheadings_name= models.CharField(null=True,verbose_name="زیر عنوان", max_length=200)

    class Meta:
        verbose_name= "زیر عنوان"
        verbose_name_plural = "زیر عناوین"
    def __str__(self):
        return self.subheadings_name


# class Membership(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    class_students = models.ForeignKey(class_room, on_delete=models.CASCADE)
#    date_joined = models.DateField(auto_now_add=True, verbose_name="تاریخ عضویت")



class Enrolled(models.Model):
    student_profile = models.ForeignKey(User, related_name='students',on_delete=models.CASCADE,  null=True, blank=True,verbose_name="نام کاربری")
    classroom = models.ForeignKey(class_room, on_delete=models.CASCADE , related_name='classroom_enroll', null=True, blank=True, verbose_name="نام کلاس")
    date =models.DateTimeField(auto_now_add=True)
    previous_attempts = models.IntegerField(default=0)
    objects = EnrolledManager()

    class Meta:
        verbose_name = "دانش آموز کلاس"
        verbose_name_plural = "دانش آموزان کلاس"


    def __unicode__(self):
        return u'{0}'.format(self.student_profile)

    @staticmethod
    def autocomplete_search_fields():
        return (
            "student_profile__user__last_name__icontains",
            "student_profile__user__first_name__icontains",)

class EnrolledTeacher(models.Model):
    teacher_profile = models.ForeignKey(User, related_name='teachers',on_delete=models.CASCADE, null=True, blank=True ,verbose_name="نام کاربری")
    tclassroom = models.ForeignKey(class_room, on_delete=models.CASCADE, related_name='classroom_enrollteacher', null=True, blank=True, verbose_name="نام کلاس")
    date = models.DateTimeField(auto_now_add=True)
    previous_attempts = models.IntegerField(default=0)
    objects = EnrolledManager()

    class Meta:
        verbose_name = "استاد کلاس"
        verbose_name_plural = "اساتید کلاس"


    def __unicode__(self):
        return u'{0}'.format(self.teacher_profile)

    @staticmethod
    def autocomplete_search_fields():
        return (
            "teacher_profile__user__last_name__icontains",
            "teacher_profile__user__first_name__icontains",)
