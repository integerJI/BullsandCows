from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.chat, name='chat'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
