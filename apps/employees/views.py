from rest_framework import generics, permissions
from .models import Employee
from .serializers import EmployeeSerializer
from apps.accounts.permissions import IsHRorAdmin


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related('user', 'department', 'designation').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsHRorAdmin]


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.select_related('user', 'department', 'designation').all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsHRorAdmin]