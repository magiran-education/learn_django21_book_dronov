from django.urls import path

from .views import index, by_rubric
from  bboard.views import BbCreateView, add, add_save


urlpatterns = [
    # path('add/', BbCreateView.as_view(), name='add'),
    path('add/', add, name='add'),
    path('add/save', add_save, name='add_save'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
