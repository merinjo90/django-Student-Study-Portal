from django.shortcuts import render
from . forms import *

# Create your views here.

#home Page
def home(request):
    return render(request,'dashboard/home.html')

#Student Notes
def notes(request):
    form =NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)