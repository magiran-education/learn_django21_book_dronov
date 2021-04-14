from django.shortcuts import render
from bboard.models import Bb


def index(request):
    context = {
        'bbs': Bb.objects.all()
    }

    return render(request, 'bboard/index.html', context)
