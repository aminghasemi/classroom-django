from django.urls import path, re_path
from .views import classroom, api, class_detail, classroom2, TeacherList



app_name="classrooms"
urlpatterns = [
    path('',classroom,name="mainpage"),
    path('classroom2',classroom2,name="mainpage2"),
    path('<slug:slug>',class_detail,name="class_details"),

    path('api',api, name="api"),
    path('teacher/<slug:username>', TeacherList.as_view(), name="teacher"),
    path('teacher/<slug:username>/page/<int:page>', TeacherList.as_view(), name="teacher"),
]
