# Register your models here.


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile

# admin.site.register(UserProfile)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ['user', 'home_address', 'phone_number']
    list_filter = []
    search_fields = ['user__username', 'home_address', 'phone_number']
    ordering = ['user__username']
    filter_horizontal = []

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj == request.user.userprofile:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj and obj == request.user.userprofile:
            return True
        return False


admin.site.register(UserProfile, UserProfileAdmin)
