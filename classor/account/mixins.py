from django.http import Http404
from django.shortcuts import get_object_or_404
from classroom.models import class_room


class EnrollMixin():
    def dispatch(self,request, *args, **kwargs):
        if request.user.student_profile__user.exists() or request.user.student_profile__user.exists() or self.request.user.is_superuser:
            new_classworks = None

        return super().dispatch(request, *args, **kwargs)
class SuperUserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما به این صفحه دسترسی ندارید.")
class CreatorAccessMixin():
    def dispatch(self, request, slug, *args, **kwargs):
        classroom= get_object_or_404(class_room, slug=slug)
        if classroom.creator == request.user or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما به این صفحه دسترسی ندارید.")
