from django.shortcuts import render
from objectiveQues.models import Ques, Subject

# Create your views here.
def q(request):
    subjects=Subject.objects.all()
    quess=Ques.objects.all()
    return render(request,"objectiveQues/ques.html",{'subjects':subjects,'quess':quess})
