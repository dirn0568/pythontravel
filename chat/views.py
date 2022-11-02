import json
import random

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
# from rest_framework.generics import GenericAPIView
# from rest_framework.response import Response
# from .serializers import ChatMatchSerializer
# from collections import deque
# Create your views here.

# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe

from chat.models import RoomJoin
from collections import deque
male_want_male = deque()
male_want_female = deque()
male_want_any = deque()
female_want_male = deque()
female_want_female = deque()
female_want_any = deque()


User = get_user_model()

def index(request):
    context = {}
    return render(request, 'index.html', context)

def room(request, room_name):
    print(room_name, '룸 네임')
    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    # print(ip, 'ip')
    return render(request, 'room.html', {
        'room_name': room_name
    })

#################################################################################################
'''def get_another(user, gender, want_match):
    print("갯어나더 실행중")
    another = 1
    return another*/



def ChatMatchView(request, pk):
    user = User.objects.filter(pk=pk)
    for temp_user in user:
        if len(RoomJoin.objects.filter(join_user=temp_user)) >= 1:
            print('이미 유저가 있네요')
        else:
            model = RoomJoin(join_user=temp_user)
            model.save()
    if len(RoomJoin.objects.all()) >= 2:
        print('어디서부터 안되는거야')
        random_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                       'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        temp_random = ''
        print('어디서부터 안되는거야2')
        for i in range(0, 30):
            y = random.randrange(36)
            print('어디서부터 안되는거야3')
            print(y, 'y')
            temp_random += random_data[y]
        print(temp_random, 'temp_random')
        return redirect('http://127.0.0.1:8000/chat_test/{0}/'.format(temp_random))
        print('이게 실행이되나')
    return render(request, 'connecting_room.html')'''

def ChatMatchView(request, room_number):
    print('그저 뷰 확인용')
    return render(request, 'connecting_room.html', {
        'room_number': room_number
    })

#ip 확인??
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(ip)
    return ip


def get_queue(user):
    return user