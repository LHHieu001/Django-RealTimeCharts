from django.urls import path
from .views import baseView

urlpatterns = [
    path('', baseView.as_view(), name='base')
]
