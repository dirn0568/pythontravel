from django.contrib import admin

from .models import Message, RoomJoin

admin.site.register(Message)

################################################################
admin.site.register(RoomJoin)