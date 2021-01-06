from django.urls import path
from breadr import views

app_name = 'breadr'

urlpatterns = [
    path('', views.index, name='index'),
    path('index.html', views.index),
]