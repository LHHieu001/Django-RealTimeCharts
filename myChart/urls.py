from django.urls import path
from . import views

urlpatterns = [
    path('', views.signInView, name='signin'),
    path('login/', views.signInView, name='signin'),
    path('base/', views.baseView.as_view(), name='base'),
    path('register/', views.signUpView, name='signup')
]
