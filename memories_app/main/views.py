from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import DetailView

from .models import Memory


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html')
    user = User.objects.get(username=request.user)
    try:
        memories = Memory.objects.all().filter(user=user)
    except models.ObjectDoesNotExist:
        memories = None
    return render(request, 'index.html', {'memories': memories})


def get_post(request):
    user = User.objects.get(username=request.user)
    title = request.POST.get('title')
    description = request.POST.get('description')
    coordinates = request.POST.get('coords')
    # lat, lon = coordinates.split(',')
    print(f'COORDINATES: {coordinates}')
    # Memory.objects.create(
    #     user=user,
    #     title=title,
    #     description=description,
    #     lat=lat,
    #     lon=lon,
    # )
    return redirect('index')


class MemoryDetailView(DetailView):
    model = Memory
    fields = '__all__'
    template_name_suffix = '_detail'
