from django.shortcuts import render, redirect


def index(request):
    return render(request, 'index.html')


def get_post(request):
    title = request.POST.get('title')
    text = request.POST.get('title')
    Memory.objects.create()
    return redirect('index')
