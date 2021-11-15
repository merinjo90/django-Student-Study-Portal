from django.shortcuts import render,redirect
from . forms import *
from django.contrib import messages
from django.views import generic

# Create your views here.

#home Page
def home(request):
    return render(request,'dashboard/home.html')

#Student Notes creation
def notes(request):
    if request.method== "POST":
        form=NotesForm(request.POST)
        if form.is_valid():
            notes =Notes(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request, f"Notes Added form {request.user.username} Successfully")
    else:
        form =NotesForm()
    notes=Notes.objects.filter(user=request.user)
    context={'notes':notes,'form':form}
    return render(request,'dashboard/notes.html',context)

#Student Notes Deletion

def delete_note(request,pk=None):
    Notes.objects.get(id=pk).delete()
    return redirect("notes")

#Detailed notes for student

class NotesDetailView(generic.DetailView):
    model=Notes

#Student HomeWorks
def homework(request):
    return render(request,'dashboard/homework.html')
