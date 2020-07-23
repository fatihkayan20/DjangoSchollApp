import mimetypes
import os
from fileinput import filename
from wsgiref.util import FileWrapper

from django.http import FileResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from reportlab.platypus import Image

from .models import *
# Create your views here.


def index(request):
    arsiv=Fotograflar.objects.all()
    fotolar=FotoImage.objects.filter(arsiv=arsiv)
    context={
        'arsiv':arsiv,
    }
    return render(request,'fotograflar/index.html',context)



def detail(request , slug ):
    arsiv = get_object_or_404(Fotograflar,slug=slug)
    fotolar=FotoImage.objects.filter(arsiv=arsiv)
    context = {
        'arsiv':arsiv,
        'fotolar': fotolar,
    }
    return render(request, 'fotograflar/detail.html', context)


def fullscreenFoto(request, id,):
    img = get_object_or_404(FotoImage, id=id)
    context = {
        'img':img,
    }
    return render(request, 'fotograflar/fullscreen.html', context)
