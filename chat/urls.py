
from django.urls import path, include

from chat import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('play/<str:room_name>/', views.room, name='room'),

    #########################################################################################################
    path('<str:room_number>/', views.ChatMatchView, name='match'),
]