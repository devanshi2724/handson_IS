from django.shortcuts import redirect, render
from operations.forms import BookForm,IncubatorDBForm
from .models import IncubatorDB
from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse



def home(request):
    return HttpResponse('Hello, World!')

def create_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else

    return render(request, 'create_book.html', {'form': form})


def new_incubator(request):
    form = IncubatorDBForm()

    if request.method == 'POST':
        form = IncubatorDBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incubator_list')  # Redirect to incubator_list page

    return render(request, 'new_incubator.html', {'form': form})

def incubator_list(request):
    incubators = IncubatorDB.objects.all()
    return render(request, 'incubator_list.html', {'incubators': incubators})

def process_selected_projects(request):
    if request.method == 'POST':
        selected_projects = request.POST.getlist('selected_projects')
        
        # Process the selected projects
        # You can perform any desired actions with the selected projects
        # such as updating the database, sending notifications, etc.
        
        # For demonstration purposes, let's pass the selected projects to a template
        context = {'selected_projects': selected_projects}
        return render(request, 'process_selected_projects.html', context)
    
    # Handle other HTTP methods if needed
    return render(request, 'error.html', {'error_message': 'Invalid request method.'})
