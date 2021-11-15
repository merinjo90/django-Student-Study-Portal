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

#Student HomeWorks Creation
def homework(request):
    if request.method == "POST":
        form = HomeworkForm(request.POST)
        if form.is_valid():
            try:
                finished = request.POST['is_finished']
                if finished == 'on':
                    finished = True
                else:
                    finished = False
            except:
                finished = False
            homeworks=Homework(
                user=request.user,
                subject=request.POST['subject'],
                title = request.POST['title'],
                description = request.POST['description'],
                due = request.POST['due'],
                is_finished = finished
            )
            homeworks.save()
            messages.success(request,f'Homework Added from {request.user.username}!!')
    else:
        form=HomeworkForm()
    homework=Homework.objects.filter(user=request.user)
    if len(homework)==0:
        homework_done=True
    else:
        homework_done=False
    context={
             'homeworks':homework,
             'homework_done':homework_done,
             'form':form
             }
    return render(request,'dashboard/homework.html',context)

#Homework Updation
def update_homework(request,pk=None):
    homework=Homework.objects.get(id=pk)
    if homework.is_finished==True:
        homework.is_finished = False
    else:
        homework.is_finished = True
    homework.save()
    return redirect('homework')

