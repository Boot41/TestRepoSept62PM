from django.test import TestCase
from django.urls import reverse
from .models import InterviewSession

class InterviewViewTests(TestCase):
    def setUp(self):
        self.invitation_code = '123456'
        InterviewSession.objects.create(invitation_code=self.invitation_code)

    def test_join_interview(self):
        response = self.client.post(reverse('join_interview'), {'fresher_name': 'John Doe', 'invitation_code': self.invitation_code})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['message'], 'Successfully joined the interview session.')
        session = InterviewSession.objects.get(invitation_code=self.invitation_code)
        self.assertEqual(session.status, 'joined')

    def test_invalid_join(self):
        response = self.client.post(reverse('join_interview'), {'fresher_name': 'John Doe', 'invitation_code': 'invalid'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'Invalid invitation code.')

    def test_interview_status(self):
        response = self.client.get(reverse('interview_status'), {'invitation_code': self.invitation_code})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'pending')

    def test_invalid_status(self):
        response = self.client.get(reverse('interview_status'), {'invitation_code': 'invalid'})
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['error'], 'Invalid invitation code.')