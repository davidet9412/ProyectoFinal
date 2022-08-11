from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Message

def index(request):
    return render(request, 'chat/index.html')

def chatroom(request, username):
    origin = request.user
    target = User.objects.get(username=username)
    messages = Message.objects.filter(origin=origin, target=target) | Message.objects.filter(origin=target, target=origin)
    messages = messages.order_by("timestamp")
    return render(request, 'chat/room.html', {
        'username': username,
        'messages': messages
    })