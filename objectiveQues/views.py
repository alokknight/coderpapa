from django.shortcuts import render
from objectiveQues.models import Ques, Subject

# Create your views here.
def q(request):
    subjects=Subject.objects.all()
    context = []
    for subject in subjects:
        questions = Ques.objects.filter(subject=subject)
        context.append({
            'subject': subject,
            'questions': questions,
        })
    return render(request,"objectiveQues/ques.html",{'context':context})

def view_subject_questions(request, subject):
    context = []
    # Get the subject object based on its name
    subject = Subject.objects.get(subject=subject)

    # Query all questions related to the subject
    questions = Ques.objects.filter(subject=subject)
    context.append({
            'subject': subject,
            'questions': questions,
        })
    context = {
        'context': context,
    }

    return render(request,"objectiveQues/ques.html",context)
