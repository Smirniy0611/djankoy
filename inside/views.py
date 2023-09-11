from django.shortcuts import render
from django.http import HttpResponse

from .models import Bd


def index(request):
    s = 'Объявления \r\n\r\n'
    for bb in Bd.objects.all():
        s += bb.title +'\r\n' + bb.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain', charset='utf-8')
