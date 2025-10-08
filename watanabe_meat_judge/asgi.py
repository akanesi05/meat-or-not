import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from judge import urls as judge_urls

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'watanabe_meat_judge.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            judge_urls.websocket_urlpatterns
        )
    ),
})