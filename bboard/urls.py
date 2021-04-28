from django.urls import path

from bboard.views import index, by_rubric, AddView


urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]
