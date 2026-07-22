from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_active_employee', 'is_staff')
    list_filter = ('role', 'is_active_employee', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', 'phone_number', 'is_active_employee')}),
    )


admin.site.register(User, CustomUserAdmin)