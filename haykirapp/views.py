from django.shortcuts import render,redirect
from . import models
from django.urls import reverse
from haykirapp.forms import AddTweetForm,AddTweetModelForm

# Create your views here.

def listhaykir(request):
    all_messages = models.Tweet.objects.all()
    tweet_dict = {"tweets":all_messages}
    return render(request,'haykirapp/listhaykir.html',context=tweet_dict)

def addhaykir(request):
    if request.method == 'POST':
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.Tweet.objects.create(nickname=nickname,message=message)
        return redirect(reverse("haykirapp:listhaykir"))
    else:
        return render(request,"haykirapp/addhaykir.html")

def addtweetbyform(request):
    if request.method == 'POST':
        form = AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('haykirapp:listhaykir'))
        else:
            print("error in form!")
            return render(request,'haykirapp/addtweetbyform.html',context={"form":form})
    else:
        form=AddTweetForm()
        return render(request,'haykirapp/addtweetbyform.html',context={"form":form})

def addtweetbymodelform(request):
     if request.method == 'POST':
        form = AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname,message=message)
            return redirect(reverse('haykirapp:listhaykir'))
        else:
            print("error in form!")
            return render(request,'haykirapp/addtweetbymodelform.html',context={"form":form})
     else:
        form=AddTweetModelForm()
        return render(request,'haykirapp/addtweetbymodelform.html',context={"form":form})

    