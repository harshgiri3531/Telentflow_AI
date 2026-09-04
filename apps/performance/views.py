from rest_framework import generics, permissions
from .models import Goal, PerformanceReview
from .serializers import GoalSerializer, PerformanceReviewSerializer
from apps.accounts.permissions import IsManager, IsHRorAdmin


class GoalListCreateView(generics.ListCreateAPIView):
    serializer_class = GoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(employee=self.request.user.employee_profile)

    def perform_create(self, serializer):
        serializer.save(employee=self.request.user.employee_profile)


class PerformanceReviewListCreateView(generics.ListCreateAPIView):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsHRorAdmin]

    def perform_create(self, serializer):
        serializer.save(reviewer=self.request.user.employee_profile)

class MyReviewsView(generics.ListAPIView):
    serializer_class = PerformanceReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PerformanceReview.objects.filter(employee=self.request.user.employee_profile)
    