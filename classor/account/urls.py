from django.contrib.auth import views
from django.urls import path,reverse
from .views import ClassesList , ClassesCreate, EnrollClass, class_comment, class_classwork, class_student, class_teacher, TeacherEnrollClass, ClassesUpdate, ClassesDelete, StudentEnrollClass
from account import views as account_views
from django.conf.urls import url



app_name = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('signup/', account_views.signup.as_view(), name='signup'),
    path('enroll/', EnrollClass.as_view(), name="enroll"),
    path('tenroll/', TeacherEnrollClass.as_view(), name="enroll_teacher"),
    path('senroll/', StudentEnrollClass.as_view(), name="enroll_student"),
    path('<slug:slug>/comments/',class_comment, name='comment'),
    path('<slug:slug>/classworks/',class_classwork, name='classwork'),
    path('<slug:slug>/students/',class_student, name='student'),
    path('<slug:slug>/teachers/',class_teacher, name='teachers'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

#    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
#    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),

#    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
#    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
#    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += [
    path('', ClassesList.as_view(),name="home"),
    path('create/', ClassesCreate.as_view(),name="class-create"),
    path('update/<slug:slug>', ClassesUpdate.as_view(),name="class-update"),
    path('delete/<slug:slug>', ClassesDelete.as_view(),name="class-delete"),


]
