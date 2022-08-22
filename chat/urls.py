
from django.urls import path, include

from chat import views

app_name = 'chat'

urlpatterns = [
    path('chat_index', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]