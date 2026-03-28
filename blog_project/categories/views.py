from django.shortcuts import redirect, render

from . import forms

# Create your views here.
def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')  # Replace 'add_category' with the actual URL name for the list view
    else:
        category_form = forms.CategoryForm()
    return render(request, 'add_categorie.html', {'form': category_form})
