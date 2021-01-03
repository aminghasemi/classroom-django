from .models import Comment, Classworks, Enrolled, EnrolledTeacher
from django import forms
from account.models import Profile
from .mixins import FieldsMixin

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body','name')

class ClassworksForm(forms.ModelForm, FieldsMixin):
    class Meta:
        model = Classworks
        fields = ('classworks_body','classworks_name')

class EnrollForm(forms.ModelForm):
    class Meta:
        model= Enrolled
        fields= ('student_profile',)

class TeacherEnrollForm(forms.ModelForm):
    class Meta:
        model= EnrolledTeacher
        fields= ('teacher_profile',)
