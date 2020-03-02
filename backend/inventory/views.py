# Create your views here.
from django.http import JsonResponse

def index(request):
    return JsonResponse({"ping": "pong"})