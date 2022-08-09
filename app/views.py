from multiprocessing import context
from django.shortcuts import render

from .forms import ViloyatForm
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')


def addviloyat(request):
    form = ViloyatForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Add Successfully !")
        return HttpResponseRedirect("/")
    context = {
        'form':form
    }


    return render(request,'addviloyat.html',context)