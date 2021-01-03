# Generated by Django 3.0.6 on 2020-06-10 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0003_auto_20200610_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_room',
            name='students',
            field=models.ManyToManyField(related_name='classstudents', through='classroom.Enrolled', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='class_room',
            name='teachers',
            field=models.ManyToManyField(related_name='classteachers', through='classroom.EnrolledTeacher', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='enrolled',
            name='student_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری'),
        ),
        migrations.AlterField(
            model_name='enrolledteacher',
            name='teacher_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to=settings.AUTH_USER_MODEL, verbose_name='نام کاربری'),
        ),
    ]