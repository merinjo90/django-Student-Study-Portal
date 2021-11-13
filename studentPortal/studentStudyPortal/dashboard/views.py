from django.shortcuts import render
from .models import Notes

# Create your views here.

#home Page
def home(request):
    return render(request,'dashboard/home.html')

#Student Notes
def notes(request):
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes}
    return render(request,'dashboard/notes.html',context)