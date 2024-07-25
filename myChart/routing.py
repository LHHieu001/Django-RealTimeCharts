from django.urls import path
from .consumers import *

ws_urlpatterns = [
    path('ws/chart/', ChartConsumer.as_asgi()),
]