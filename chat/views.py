import json

from django.shortcuts import render

# Create your views here.

# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe


def index(request):
    context = {}
    return render(request, 'index.html', context)

def room(request, room_name):
    print(room_name, '룸 네임')
    return render(request, 'room.html', {
        'room_name': room_name
    })