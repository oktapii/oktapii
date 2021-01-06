from django.urls import path
from breadr import views

app_name = 'breadr'

handler404 = 'breadr.views.err404'

urlpatterns = [
    path('', views.index, name='index'),
]