from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    is_teacher=models.BooleanField(default=False, verbose_name= "وضعیت استاد")
    is_student=models.BooleanField(default=False, verbose_name= "وضعیت استاد")
    special_teacher=models.DateTimeField(default=timezone.now, verbose_name ="استاد ویژه تا")

    def is_special_teacher(self):
        if self.special_teacher > timezone.now():
            return True
        else:
            return False
    is_special_teacher.boolean = True
    is_special_teacher.short_description = "وضعیت استاد ویژه"

class Profile(models.Model):
    STUDENT=1
    TEACHER=2
    ADVISOR=3
    SCHOOL=4
    CONTRIBUTER=5
    ADMIN=6

    ROLE_CHOICES = (
        (STUDENT, 'دانش آموز'),
        (TEACHER, 'استاد'),
        (ADVISOR, 'مشاور'),
        (SCHOOL, 'آموزشگاه'),
        (CONTRIBUTER, 'وبمستر'),
        (ADMIN, 'ادمین'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True, verbose_name='نقش')
    user = models.OneToOneField(User,unique=True, null=True, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, verbose_name='درباره کاربر')
    location = models.CharField(max_length=30, blank=True, verbose_name='شهرستان')
    birth_date = models.DateField(null=True, blank=True, verbose_name='تاریخ تولید')
    phone_number=models.CharField(max_length=11,unique=True, null=True, verbose_name='شماره همراه')
    national_code=models.IntegerField(max_length=10,unique=True, null=True, verbose_name='کد ملی')



    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

#@receiver(post_save, sender=User)
#def update_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Profile.objects.create(user=instance)
#    instance.profile.save()

#    class Role(models.Model):
#        STUDENT=1
#        TEACHER=2
#        ADVISOR=3
#        SCHOOL=4
#        CONTRIBUTER=5
#        ADMIN=6
#
#        ROLE_CHOICES = (
#            (STUDENT, 'دانش آموز'),
#            (TEACHER, 'استاد'),
#            (ADVISOR, 'مشاور'),
#            (SCHOOL, 'آموزشگاه'),
#            (CONTRIBUTER, 'وبمستر'),
#            (ADMIN, 'ادمین'),
#        )
#        id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#        def __str__(self):
#          return self.get_id_display()
