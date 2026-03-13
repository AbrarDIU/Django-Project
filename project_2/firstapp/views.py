from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    # return HttpResponse("This Is Home Page")
    return render(request, "firstapp/home.html")