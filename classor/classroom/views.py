from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from .models import class_room
from account.models import User
# Create your views here.

def classroom(request):
    context={
        "Class": class_room.objects.all()
    }
    return render(request,"classroom/classroom.html", context)

def classroom2(request):
    context={
        "Class": class_room.objects.all()
    }
    return render(request,"classroom/classroom2.html", context)




def class_detail(request, slug):

    context={
            "Classdetails": get_object_or_404(class_room, slug=slug)
}
    return render(request,"classroom/post2.html", context)




class TeacherList(ListView):
    paginate_by = 5
    template_name = 'classroom/teacher_list.html'

    def get_queryset(self):
        global teacher_list
        username = self.kwargs.get('username')
        teacher = get_object_or_404(User, username=username)
        return teacher.articles.published()

    def get_context_data(self, **kwargs):
        context = super().get_context.data(**kwargs)
        context['teacher'] = teacher
        return context








def api(request):
    data= {
        "1": {
        "title": "hinew2",
        "id": 202,
        "slug": "first code"
        },
        "2": {
        "title": "hinew3",
        "id": 220,
        "slug": "sec code"
        },
        "3": {
        "title": "hinew",
        "id": 2220,
        "slug": "third code"
        },
    }
    return JsonResponse(data)
