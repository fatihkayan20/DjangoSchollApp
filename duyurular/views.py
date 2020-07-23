from django.shortcuts import render,get_object_or_404
from .models import *
# Create your views here.

def index(request):
    notifications=Notification.objects.all().order_by('-publish_date')

    context={
        'notifications':notifications
    }
    return render(request,'duyurular/index.html',context)


def detail(request, slug):
    notification=get_object_or_404(Notification , slug=slug)
    context={
        'notification':notification
    }
    return render(request,'duyurular/detail.html',context)
