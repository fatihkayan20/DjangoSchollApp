from datetime import time, datetime

from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.

def index(request):
    izinler = Permission.objects.all()

    context = {
        'izin': izinler
    }

    return render(request, 'izinler/index.html', context)


def detail(request, slug):
    izin = get_object_or_404(Permission, slug=slug)
    accepted = izin.accept.all()
    vetod = izin.veto.all()
    message = ''
    color = ''

    date=izin.event_start_date
    now = datetime.now()

    if date.replace(tzinfo=None)>now.replace(tzinfo=None):
        oy='d-block'
        uyarı='d-none'
    else:
        oy = 'd-none'
        uyarı = 'd-block'

    ############# Onay  ##############
    if request.POST.get('submit') == 'accept':
        if request.user in izin.accept.all():
            message = 'Zaten kabul etmişsiniz'
            color = 'text-warning'
        else:
            if request.user in izin.veto.all():
                color = 'text-success'
                message = 'Oyunuz kabul olarak değiştirildi'
                izin.accept.add(request.user)
                izin.veto.remove(request.user)
                izin.save()
            else:
                color = 'text-success'
                message = 'Kabul oyunu verdiniz'
                izin.accept.add(request.user)
                izin.save()

    ############# RED  ##############
    if request.POST.get('submit') == 'veto':
        if request.user in izin.veto.all():
            message = 'Zaten reddetmişsiniz'
            color = 'text-warning'
        else:
            if request.user in izin.accept.all():
                color = 'text-success'
                message = 'Oyunuz red olarak değiştirildi'
                izin.accept.remove(request.user)
                izin.veto.add(request.user)
                izin.save()
            else:
                color = 'text-success'
                message = 'Red oyunu verdiniz'
                izin.veto.add(request.user)
                izin.save()
    context = {
        'izin': izin,
        'message': message,
        'color': color,
        'accepted': accepted,
        'vetod': vetod,
        'oy':oy,
        'uyarı':uyarı,
    }
    return render(request, 'izinler/detail.html', context)
