# chat/consumers.py
from datetime import time

from asgiref.sync import async_to_sync

import json

from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from django.http import request

from chat.models import Message


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        print(self.room_name, 'self.room_name') #방 이름
        print(self.room_group_name, 'self.room_group_name') #chat + 방이름

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        ) # 채널에 추가??
        print(self.channel_name, 'self.channel_name') #그냥 채널의 이름??
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        ) # 추가된 채널 삭제??

    # Receive message from WebSocket
    def receive(self, text_data):
        print(text_data, 'text_data')
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        author = text_data_json["author"]

        print(author, "author")
        print(message, "message")
        user_instance = User.objects.filter(username=author)[0]
        model = Message(author=user_instance,
                        content=message)
        model.save()
        print(user_instance.username, 'username')
        user_name = user_instance.username
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, 'user_name': user_name}
        )

    # Receive message from room group
    def chat_message(self, event):
        print(event, "event")
        message = event["message"]
        user_name = event["user_name"]

        # Send message to WebSocket
        async_to_sync(self.send(text_data=json.dumps({"message": message, 'user_name': user_name})))