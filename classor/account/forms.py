from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    STUDENT=1
    TEACHER=2
    ADVISOR=3
    SCHOOL=4
    ROLE_CHOICES = (
        (STUDENT, 'دانش آموز'),
        (TEACHER, 'استاد'),
        (ADVISOR, 'مشاور'),
        (SCHOOL, 'آموزشگاه'),
    )
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD',)
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email','role', 'password1', 'password2', )
