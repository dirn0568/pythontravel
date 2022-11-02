from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/chat_test/(?P<room_number>\w+)/$', consumers.ChatConnect),
    ###############################################################################################################

    re_path(r'ws/chat_test/play/(?P<room_name>\w+)/$', consumers.ChatConsumer),

]