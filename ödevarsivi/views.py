
from django.http import FileResponse
from django.shortcuts import render, get_object_or_404
from .models import *



# Create your views here.

def index(request):
    odevler = Odevler.objects.all()
    context = {
        'odev': odevler
    }
    return render(request, 'ödevler/index.html', context)

def detail(request, slug):
    odev=get_object_or_404(Odevler,slug=slug)

    return FileResponse(open('media/'+odev.file.name,'rb'),content_type='app/pdf')