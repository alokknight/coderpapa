from django.shortcuts import render
from wineshop.models import Wine
from datetime import datetime
from django.contrib import messages
# Create your views here.


def wineshop(request):
    wines=Wine.objects.all()
    return render(request,"wineshop/wineshop.html",{'wines':wines})

