from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_post', views.get_post, name='get_post'),
]
