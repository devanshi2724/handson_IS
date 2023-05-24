from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        
class IncubatorDBForm(forms.ModelForm):
    class Meta:
        model = IncubatorDB
        fields = '__all__'