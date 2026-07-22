from rest_framework import serializers
from .models import Employee
from apps.accounts.serializers import UserSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    designation_title = serializers.CharField(source='designation.title', read_only=True)

    class Meta:
        model = Employee
        fields = (
            'id', 'user', 'user_detail', 'employee_id',
            'department', 'department_name',
            'designation', 'designation_title',
            'manager', 'date_of_joining', 'date_of_leaving', 'status',
        )