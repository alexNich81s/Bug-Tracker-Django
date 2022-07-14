from django.shortcuts import render, redirect, reverse
from .models import Bug
from .forms import CreateBugForm

# Create your views here.
def home_view(request):
    list_bugs = Bug.objects.all()
    context = {
        'bug_list': list_bugs
    }
    
    return render(request, 'home.html', context)

def create_bug(request):
    if request.method == 'POST':
        form = CreateBugForm(request.POST)
        if form.is_valid():
            bug = form.save(commit = False)
            bug.save()
    else:
        form = CreateBugForm()

    context={
         'form' :form
    }
    return render(request, 'create_bug.html', context)