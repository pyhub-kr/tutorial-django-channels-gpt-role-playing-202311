import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django_asgi_app = get_asgi_application()

# app.routing 임포트는 여기에 !!!
# 🔥 HERE
import chat.routing  # noqa

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    # 🔥 HERE
    "websocket": URLRouter(
        chat.routing.websocket_urlpatterns
    ),
})
