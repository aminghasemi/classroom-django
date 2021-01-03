from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

UserAdmin.fieldsets[2][1]['fields'] = ('is_active', 'is_staff', 'is_superuser','is_teacher', 'groups', 'user_permissions',)
UserAdmin.list_display += ('is_teacher',)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'پروفایل'
    fk_name = 'user'
    verbose_name= 'پروفایل'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



admin.site.register(User, CustomUserAdmin)

# Register your models here.
