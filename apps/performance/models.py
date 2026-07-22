from django.db import models
from apps.employees.models import Employee


class Goal(models.Model):
    class GoalStatus(models.TextChoices):
        IN_PROGRESS = 'IN_PROGRESS', 'In Progress'
        COMPLETED = 'COMPLETED', 'Completed'
        MISSED = 'MISSED', 'Missed'

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='goals')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=GoalStatus.choices, default=GoalStatus.IN_PROGRESS)

    def __str__(self):
        return f"{self.title} - {self.employee.employee_id}"


class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, related_name='reviews_given')
    rating = models.PositiveSmallIntegerField()  # 1-5 scale
    feedback = models.TextField()
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.employee.employee_id} by {self.reviewer}"