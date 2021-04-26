from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from bboard.models import Bb, Rubric
from bboard.forms import BbForm


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


def add(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(
                reverse_lazy(
                   'by_rubric',
                   kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}
                )
            )
        else:
            context = {
                'form': bbf,
                'rubrics': Rubric.objects.all(),
            }
            return render(request, 'bboard/create.html', context)
    else:
        bbf = BbForm()
        context = {
            'form': bbf,
            'rubrics': Rubric.objects.all(),
        }
        return render(request, 'bboard/create.html', context)
