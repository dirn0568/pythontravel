# chat/consumers.py
from datetime import time

from asgiref.sync import async_to_sync

import json

from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from django.http import request

from chat.models import Message

from . import views


class ChatConsumer(WebsocketConsumer):
    print('챗컨슈머 성공')
    def connect(self):
        print('챗컨슈머 성공2')
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        #print(self.room_name, 'self.room_name') #방 이름
        #print(self.room_group_name, 'self.room_group_name') #chat + 방이름

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        ) # 채널에 추가??
        #print(self.channel_name, 'self.channel_name') #그냥 채널의 이름??
        self.accept()

    def disconnect(self, close_code):
        print('챗컨슈머 성공3')
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        ) # 추가된 채널 삭제??

    # Receive message from WebSocket
    def receive(self, text_data):
        print('챗컨슈머 성공44')
        print(text_data, 'text_data')
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        author = text_data_json["author"]

        user_instance = User.objects.filter(username=author)[0]
        model = Message(author=user_instance,
                        content=message)
        model.save()
        user_name = user_instance.username
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, 'user_name': user_name}
        )

    # Receive message from room group
    def chat_message(self, event):
        print('챗컨슈머 성공5')
        message = event["message"]
        user_name = event["user_name"]

        # Send message to WebSocket
        async_to_sync(self.send(text_data=json.dumps({"message": message, 'user_name': user_name})))




########################################################################################################################

class ChatConnect(WebsocketConsumer):
    print('쳇커넥트성곡')

    def get_user_info(self):
        pk = self.scope['user'].pk
        user = User.objects.get(pk=pk)
        return user

    def connect(self):
        """
        본인의 큐를 찾고 내 앞의 대기자수를 반환
        """
        user = self.get_user_info()
        print(user, 'user')
        self.my_queue = views.get_queue(user)
        print(self.my_queue, 'self.my_queue')
        try:
            count = self.my_queue.index(user)
        except:
            count = 0
        print(count, 'count')
        self.room_group_name = user

        # Join room group
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({
            'waiters_count': count,
        }))
        print(count, "커넥트 여기까지 나오나요")

    #################################################################################3333333333333333333333
    # def connect(self):
    #     print('ChatConnect 성공2')
    #     self.room_number = self.scope["url_route"]["kwargs"]["room_number"]
    #     self.room_group_number = "chat_%s" % self.room_number
    #     #print(self.room_name, 'self.room_name') #방 이름
    #     #print(self.room_group_name, 'self.room_group_name') #chat + 방이름
    #
    #     # Join room group
    #     async_to_sync(self.channel_layer.group_add)(
    #         self.room_group_number,
    #         self.channel_name
    #     ) # 채널에 추가??
    #     #print(self.channel_name, 'self.channel_name') #그냥 채널의 이름??
    #     self.accept()

    def disconnect(self, close_code):
        print('ChatConnect 성공3')
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        ) # 추가된 채널 삭제??

    def receive(self, text_data):
        print('ChatConnect 성공44')
        print(text_data, 'text_data')
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        author = text_data_json["author"]

        user_instance = User.objects.filter(username=author)[0]
        model = Message(author=user_instance,
                        content=message)
        model.save()
        user_name = user_instance.username
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, 'user_name': user_name}
        )

    # Receive message from room group
    def chat_message(self, event):
        print('ChatConnect 성공5')
        message = event["message"]
        user_name = event["user_name"]

        # Send message to WebSocket
        async_to_sync(self.send(text_data=json.dumps({"message": message, 'user_name': user_name})))
