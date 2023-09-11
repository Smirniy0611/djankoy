from django.shortcuts import render
from django.http import HttpResponse

from .models import Bd


def index(request):
    s = 'Объявление'
    for bb in Bd.objects.all():
        s += bb.title + bb.content
    return HttpResponse(s)
