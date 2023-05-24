from django.shortcuts import render
from operations.forms import BookForm,IncubatorDBForm
from .models import IncubatorDB


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
            # Redirect to a success page or do something else

    return render(request, 'new_incubator.html', {'form': form})

def incubator_list(request):
    incubators = IncubatorDB.objects.all()
    return render(request, 'incubator_list.html', {'incubators': incubators})