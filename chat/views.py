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
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip, 'ip')
    return render(request, 'room.html', {
        'room_name': room_name
    })


def connecting(request):
    request.user
    print()
    pass



#ip 확인??
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return ip