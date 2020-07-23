from django.shortcuts import render
from ödevarsivi.models import *
from fotografarsivi.models import *
# Create your views here.

def index(request):
    odevler=Odevler.objects.all().order_by('-published_date')[0:5]
    fotolor=Fotograflar.objects.all().order_by('-published_date')[0:5]
    context={
        'odev':odevler,
        'fotolor':fotolor,
    }
    return render(request,'anasayfa/index.html',context)