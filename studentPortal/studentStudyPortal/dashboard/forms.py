from django import forms
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model=Notes
        fields=['title','description']

class DateInput(forms.DateInput):
    input_type = 'date'

#homework form
class HomeworkForm(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']

#commn form- wikkipedia,dictionary,youtube,book search form
class DashboardForm(forms.Form):
    text=forms.CharField(max_length=100,label="Enter your search :")

#to-do form
class TodoForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields=['title','is_finished']

#conversion form
class ConversionForm(forms.Form):
    CHOICES=[('length''Length'),('mass','Mass')]
    measurement=forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)