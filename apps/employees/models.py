from django.db import models
from django.conf import settings
from apps.organizations.models import Department, Designation


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employee_profile'
    )
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True, related_name='employees'
    )
    designation = models.ForeignKey(
        Designation, on_delete=models.SET_NULL, null=True, related_name='employees'
    )
    manager = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='team_members'
    )
    date_of_joining = models.DateField()
    date_of_leaving = models.DateField(null=True, blank=True)

    class EmploymentStatus(models.TextChoices):
        ACTIVE = 'ACTIVE', 'Active'
        ON_LEAVE = 'ON_LEAVE', 'On Leave'
        TERMINATED = 'TERMINATED', 'Terminated'
        RESIGNED = 'RESIGNED', 'Resigned'

    status = models.CharField(
        max_length=20, choices=EmploymentStatus.choices, default=EmploymentStatus.ACTIVE
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id} - {self.user.username}"