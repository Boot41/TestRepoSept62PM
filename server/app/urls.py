from django.urls import path
from .views import JoinInterviewView, InterviewStatusView

urlpatterns = [
    path('join/', JoinInterviewView.as_view(), name='join_interview'),
    path('status/', InterviewStatusView.as_view(), name='interview_status'),
]