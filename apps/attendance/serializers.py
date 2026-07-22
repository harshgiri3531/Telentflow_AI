from rest_framework import serializers
from .models import Attendance, LeaveRequest


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('id', 'employee', 'date', 'check_in', 'check_out')
        read_only_fields = ('employee',)


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = (
            'id', 'employee', 'start_date', 'end_date',
            'reason', 'status', 'approved_by', 'created_at',
        )
        read_only_fields = ('employee', 'status', 'approved_by')