from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_post', views.get_post, name='get_post'),
    path('memories/<int:pk>', views.MemoryDetailView.as_view(), name='memory-detail'),
]
