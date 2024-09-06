from django.db import models

class InterviewSession(models.Model):
    fresher_name = models.CharField(max_length=255)
    invitation_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=20, default='pending')  # e.g. 'pending', 'joined', 'completed'
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"InterviewSession({self.fresher_name}, {self.invitation_code}, {self.status})"