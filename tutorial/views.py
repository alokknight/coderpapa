from django.shortcuts import render
from tutorial.models import Tutorial
# Create your views here.
def showAllTutorial(request):
    tuts=Tutorial.objects.all()
    return render(request,'tutorial/tutorials.html', {'tuts':tuts} )

def showTutorial(request,slug):
    tutorial=Tutorial.objects.get(slug=slug)
    return render(request,'tutorial/tutorial.html', {'tutorial':tutorial} )