from django.shortcuts import render
from .models import Room

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request,'main2/home.html', context)

def room(request, pk):
    rooms = None
    for i in room:
        if i['id'] == int(pk):
            room = i,
    context = {'room': room}
    return render(request,'main2/room.html', context)