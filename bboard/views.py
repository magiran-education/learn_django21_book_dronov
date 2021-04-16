from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()

        return context
