from django.http import JsonResponse
from django.views import View
from .models import InterviewSession

class JoinInterviewView(View):
    def post(self, request):
        fresher_name = request.POST.get('fresher_name')
        invitation_code = request.POST.get('invitation_code')
        try:
            session = InterviewSession.objects.get(invitation_code=invitation_code)
            session.status = 'joined'
            session.fresher_name = fresher_name
            session.save()
            return JsonResponse({'message': 'Successfully joined the interview session.'}, status=200)
        except InterviewSession.DoesNotExist:
            return JsonResponse({'error': 'Invalid invitation code.'}, status=404)

class InterviewStatusView(View):
    def get(self, request):
        invitation_code = request.GET.get('invitation_code')
        try:
            session = InterviewSession.objects.get(invitation_code=invitation_code)
            return JsonResponse({'status': session.status}, status=200)
        except InterviewSession.DoesNotExist:
            return JsonResponse({'error': 'Invalid invitation code.'}, status=404)