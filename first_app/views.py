
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("This Is Courses page")