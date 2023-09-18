from django.shortcuts import render

from .models import Bd


def index(request):
    bbs = Bd.objects.all()
    return render(request, 'inside/index.html', {'bbs':bbs})

