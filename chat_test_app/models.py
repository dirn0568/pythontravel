from django.contrib.auth.models import User

# Create your models here.
from django.db import models

class Test_Message(models.Model):
    author_user = models.ForeignKey(User, related_name='author_user', on_delete=models.CASCADE)
    content_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)