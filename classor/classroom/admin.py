from django.contrib import admin
from.models import class_room, Comment, Classworks, Headings, SubHeadings, Enrolled, EnrolledTeacher

#admin header changes:
admin.site.site_header = "داشبورد مدیریتی کلاسور"

# Register your models here.
class class_room_admin(admin.ModelAdmin):
    list_display= ('Name','class_number','creator','status')
    list_filter= ('Name',)
    search_fields= ('Name','section')

admin.site.register(class_room,class_room_admin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'jcreated_on')
#    list_filter = ('jcreated_on',)
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

@admin.register(Classworks)
class classworksAdmin(admin.ModelAdmin):
    list_display = ('classworks_name', 'classworks_body', 'classworks_post', 'classworks_jcreated_on')
#    list_filter = ('classworks_jcreated_on',)
    search_fields = ('classworks_name', 'classworks_body')
    actions = ['approve_classworks']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
class Headings_admin(admin.ModelAdmin):
    list_display= ('headings_name',)
    list_filter= ('headings_name',)
    search_fields= ('headings_name',)

admin.site.register(Headings,Headings_admin)


class Subheadings_admin(admin.ModelAdmin):
    list_display= ('subheadings_name',)
    list_filter= ('subheadings_name',)
    search_fields= ('subheadings_name',)

admin.site.register(SubHeadings,Subheadings_admin)




@admin.register(Enrolled)
class EnrolledAdmin(admin.ModelAdmin):
    list_display= ('student_profile','classroom')
    list_filter = ('classroom', )
    search_fields = ( 'classroom', )
    autocomplete_lookup_fields = {
        'fk': ['classroom', ],
    }

#    def get_queryset(self, request):
#        qs = super(EnrolledAdmin, self).get_queryset(request)
#        qs = qs.order_by('student_profile__user__last_name', 'student_profile__user__first_name')
#        return qs

#    def student_last_name(self, obj):
#        return obj.student_profile.user.last_name.title()
#    student_last_name.short_description = ("نام خانوادگی")

#    def student_first_name(self, obj):
#        return obj.student_profile.user.first_name.title()
#    student_first_name.short_description = ("نام")




@admin.register(EnrolledTeacher)
class EnrolledTeacherAdmin(admin.ModelAdmin):
    list_display= ('teacher_profile','tclassroom')
    list_filter = ('tclassroom', )
    search_fields = ( 'tclassroom', )
    autocomplete_lookup_fields = {
        'fk': ['tclassroom', ],
    }

#    def get_queryset(self, request):
#        qs = super(EnrolledTeacherAdmin, self).get_queryset(request)
#        qs = qs.order_by('teacher_profile__user__last_name', 'teacher_profile__user__first_name')
#        return qs
#
#    def teacher_last_name(self, obj):
#        return obj.teacher_profile.user.last_name.title()
#    teacher_last_name.short_description = ("نام خانوادگی")
#
#    def teacher_first_name(self, obj):
#        return obj.teacher_profile.user.first_name.title()
#    teacher_first_name.short_description = ("نام")
