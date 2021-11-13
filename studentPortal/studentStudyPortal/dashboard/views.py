from django.shortcuts import render

# Create your views here.

#home Page
def home(request):
    return render(request,'dashboard/home.html')

#Student Notes
def notes(request):
    return render(request,'dashboard/notes.html')