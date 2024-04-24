from django.shortcuts import render
from . import models

# Create your views here.

def listhaykir(request):
    all_messages = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_messages}
    return render(request,'haykirapp/listhaykir.html',context=tweet_dict)

def addhaykir(request):
    if request.method == 'POST':
        print(request.POST["nickname"])
    return render(request,"haykirapp/addhaykir.html")