from rest_framework import serializers
from .models import Attendance, LeaveRequest


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'employee', 'date', 'check_in', 'check_out')
        read_only_fields = ('employee',)


class LeaveRequestSerializer(serializers.ModelSerializer):
    employee_name = serializers.CharField(source='employee.user.username', read_only=True)
    employee_code = serializers.CharField(source='employee.employee_id', read_only=True)

    class Meta:
        model = LeaveRequest
        fields = (
            'id', 'employee', 'employee_name', 'employee_code',
            'start_date', 'end_date', 'reason', 'status', 'approved_by', 'created_at',
        )
        read_only_fields = ('employee', 'status', 'approved_by')