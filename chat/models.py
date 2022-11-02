from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]


#####################################################################################################################
class RoomJoin(models.Model):
    join_user = models.OneToOneField(User, related_name='join_user', on_delete=models.CASCADE)

'''class RoomName(models.Model):
    room_name = models.CharField(max_length=100)
    join_user1 = models.OneToOneField(User, related_name='join_user1', on_delete=models.CASCADE)
    join_user2 = models.OneToOneField(User, related_name='join_user2', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)'''