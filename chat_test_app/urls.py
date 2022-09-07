from django.contrib import admin
from django.urls import path, include

from chat_test_app import views

app_name = 'chat_test_app'

urlpatterns = [
    path('state', views.stateview, name='stateview'),
    path('connecting', views.connectview, name='connectview'),
    path('test_room/<str:room_name>/', views.test_room, name='test_room'),
]