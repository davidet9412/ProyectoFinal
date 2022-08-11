import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from chat.models import Message
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = self.scope['url_route']['kwargs']['username']
        

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        origin = User.objects.get(username=text_data_json['from'])
        target = User.objects.get(username=text_data_json['to'])

        new_message = Message(text=message, origin=origin, target=target)        
        new_message.save()

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'origin': origin.username,
                'target': target.username
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        origin = event['origin']
        target = event['target']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'origin': origin,
            'target': target

        }))
