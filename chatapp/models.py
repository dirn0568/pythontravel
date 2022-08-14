from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class ChatModel(models.Model):
    send_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_user')
    receive_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_user')

    chat_line = models.CharField(max_length=300, null=True, blank=True)
    chat_img = models.FileField(upload_to='chat_file/', null=True, blank=True)
    chat_img_name = models.CharField(max_length=50, null=True, blank=True)
    chat_img_ext = models.CharField(max_length=50, null=True, blank=True)

    chat_time = models.DateTimeField(auto_now=True)