"""
ASGI config for pythontravel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import os #

from channels.auth import AuthMiddlewareStack #
from channels.routing import ProtocolTypeRouter, URLRouter #
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application #

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pythontravel.settings") #
# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

import chat.routing

class CustomSocketioProtocolTypeRouter(ProtocolTypeRouter):
    """
    Overrided base class's __call__ method to support python socketio 4.2.0 and daphne 2.3.0
    """
    def __call__(self, scope, *args):
        if scope["type"] in self.application_mapping:
            handlerobj = self.application_mapping[scope["type"]](scope)
            if args:
                return handlerobj(*args)
            return handlerobj
        raise ValueError(
            "No application configured for scope type %r" % scope["type"]
        )

application = CustomSocketioProtocolTypeRouter({
    # (http->django views is added by default)
    # (http->django views is added by default)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})


# application = ProtocolTypeRouter(
#     {
#         "http": django_asgi_app,
#         "websocket": AllowedHostsOriginValidator(
#             AuthMiddlewareStack(URLRouter(chat.routing.websocket_urlpatterns))
#         ),
#     }
# )





# import os
#
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
# from django.core.asgi import get_asgi_application
# django_asgi_app = get_asgi_application()
#
# import chat.routing
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pythontravel.settings')
#
# application = ProtocolTypeRouter({
#     "http": django_asgi_app,
#     "websocket": AllowedHostsOriginValidator(
#         AuthMiddlewareStack(
#             URLRouter(
#                 chat.routing.websocket_urlpatterns
#             )
#         )
#     ),
# })
