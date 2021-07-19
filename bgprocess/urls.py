from django.contrib import admin
from django.urls import path
from .views import SendMailAPIView

urlpatterns = [
    path('send-mail', SendMailAPIView.as_view(), name='sendmail'),
]