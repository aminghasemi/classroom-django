import datetime
from django.db import models
from django.db.models import Q


class EnrolledManager(models.Manager):
    def get_current_enrollments(self, profile_id):
        return super(EnrolledManager, self).get_queryset().filter(
            student_profile==profile_id).filter(
            Q(dictation__date_to__gte=datetime.datetime.now) | Q(class_room__date_to=None))

    def get_previous_enrollments(self, profile_id):
        return super(EnrolledManager, self).get_queryset().filter(
            student_profile=srofile_id,
            dictation__date_to__lt=datetime.datetime.now)
