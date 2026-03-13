from django.shortcuts import render

# Create your views here.
def home(request):
    d = {
        'name': 'Abrar',
        'age': 22,
        'hobbies': ['coding', 'gaming', 'traveling'],}
    return render(request, 'home.html', context=d)