from django.urls import path
from .views import GoalListCreateView, PerformanceReviewListCreateView

urlpatterns = [
    path('goals/', GoalListCreateView.as_view(), name='goal-list-create'),
    path('reviews/', PerformanceReviewListCreateView.as_view(), name='review-list-create'),
]