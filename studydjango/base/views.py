from django.shortcuts import render
from .models import Room


# Create your views here.

# rooms = [
#     {'id': 1, 'name': 'let me in please'},
#     {'id': 2, 'name': 'adam oscar'},
#     {'id': 3, 'name': 'adam bell'},
# ]


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'baseTemplates/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'baseTemplates/room.html', context)


def createRoom(request):
    contex = {}
    return render(request, 'baseTemplates/room_form.html', contex)
