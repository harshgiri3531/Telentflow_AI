from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'department', 'designation', 'status', 'date_of_joining')
    list_filter = ('status', 'department', 'designation')
    search_fields = ('employee_id', 'user__username')