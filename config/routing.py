from django.urls import path

from vinipoonpn.chats.consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi()),
    path("<conversation_name>/", ChatConsumer.as_asgi()),
]
