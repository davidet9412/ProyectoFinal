from django.urls import path
from chat.views import *

urlpatterns = [
    path('<str:username>/', chatroom, name='chatroom')
]