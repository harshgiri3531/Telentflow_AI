from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from .models import Attendance, LeaveRequest
from .serializers import AttendanceSerializer, LeaveRequestSerializer
from apps.accounts.permissions import IsHRorAdmin
from apps.notifications.models import Notification


class CheckInView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        employee = request.user.employee_profile
        today = timezone.localdate()
        attendance, created = Attendance.objects.get_or_create(
            employee=employee, date=today,
            defaults={'check_in': timezone.localtime().time()}
        )
        if not created and not attendance.check_in:
            attendance.check_in = timezone.localtime().time()
            attendance.save()
        return Response(AttendanceSerializer(attendance).data)


class CheckOutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        employee = request.user.employee_profile
        today = timezone.localdate()
        try:
            attendance = Attendance.objects.get(employee=employee, date=today)
            attendance.check_out = timezone.localtime().time()
            attendance.save()
            return Response(AttendanceSerializer(attendance).data)
        except Attendance.DoesNotExist:
            return Response({"detail": "No check-in found for today."}, status=400)


class LeaveRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(employee=self.request.user.employee_profile)

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user.employee_profile)


class LeaveApprovalView(generics.UpdateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsHRorAdmin]

    def perform_update(self, serializer):
        leave = serializer.save(approved_by=self.request.user.employee_profile)
        Notification.objects.create(
            recipient=leave.employee.user,
            message=f"Your leave request ({leave.start_date} to {leave.end_date}) has been {leave.status.lower()}."
        )

class AllLeaveRequestsView(generics.ListAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsHRorAdmin]

    def get_queryset(self):
        queryset = LeaveRequest.objects.select_related('employee', 'employee__user').all()
        status_param = self.request.query_params.get('status')
        if status_param:
            queryset = queryset.filter(status=status_param)
        return queryset.order_by('-created_at')