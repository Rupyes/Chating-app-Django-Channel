from django.urls import path, re_path

from . import views

app_name = "chat"

urlpatterns = [
    path('', views.index, name="index"),
    re_path(r'^chat/(?P<room_name>[^/]+)/$', views.room, name='room'),
]
