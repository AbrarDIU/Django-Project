from django.shortcuts import redirect, render

from .models import Post
from . import forms
from . import views
from . import models
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form': post_form})

def edit_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('home')
    else:
        post_form = forms.PostForm(instance=post)
    return render(request, 'add_post.html', {'form': post_form})

def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('home')
