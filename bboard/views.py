from django.shortcuts import render
from bboard.models import Bb, Rubric


def index(request):
    context = {
        'bbs': Bb.objects.all(),
        'rubrics': Rubric.objects.all(),
    }

    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    context = {
        'bbs': Bb.objects.filter(rubric=rubric_id),
        'rubrics': Rubric.objects.all(),
        'current_rubric': Rubric.objects.get(pk=rubric_id),
    }

    return render(request, 'bboard/by_rubric.html', context)
