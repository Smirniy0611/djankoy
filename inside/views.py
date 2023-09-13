from django.shortcuts import render

from .models import Bd


def index(request):
    bbs = Bd.objects.order_by('-published')
    return render(request, 'inside/index.html', {'bbs':bbs})

