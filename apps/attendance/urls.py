from django.urls import path
from .views import CheckInView, CheckOutView, LeaveRequestListCreateView, LeaveApprovalView, AllLeaveRequestsView

urlpatterns = [
    path('check-in/', CheckInView.as_view(), name='check-in'),
    path('check-out/', CheckOutView.as_view(), name='check-out'),
    path('leave/', LeaveRequestListCreateView.as_view(), name='leave-list-create'),
    path('leave/all/', AllLeaveRequestsView.as_view(), name='leave-all'),
    path('leave/<int:pk>/approve/', LeaveApprovalView.as_view(), name='leave-approve'),
]