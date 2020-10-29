from django.shortcuts import render, redirect, get_object_or_404
from .models import ProjectPost

from .forms import ProjectForm
from django.contrib import messages

def index(request):
    userid = request.user.id
    context = {
        'projects': ProjectPost.objects.all(),
    }
    return render(request, 'home.html', context)

def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'successfully added')
            return redirect('core:index')
    else:
        form = ProjectForm()
    return render(request, 'add_project.html', {'form': form, 'messages': messages})

