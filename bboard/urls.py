from django.urls import path

from .views import index, by_rubric
from  bboard.views import add


urlpatterns = [
    path('add/', add, name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
