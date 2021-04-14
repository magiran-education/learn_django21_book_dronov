from django.http import HttpResponse
from bboard.models import Bb


def index(request):
    html = 'Список объявлений\r\n\r\n\r\n'
    for b in Bb.objects.order_by('-published'):
        html += f'{b.title}\r\n{b.content}\r\n\r\n'
    return HttpResponse(html, content_type='text/plain; charset=utf-8')
