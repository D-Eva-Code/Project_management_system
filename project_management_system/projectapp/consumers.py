import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.template.loader import get_template
from django.template.loader import render_to_string

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        # print(self.channel_name)
       
        user= self.scope['user']

        # if not user.is_authenticated or user.role != "supervisor":
        #     self.close()
        #     return
        
        self.group_name= f"supervisor_{user.id}"

        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )
        pass

    def file_uploaded(self, event):
        # self.send(text_data=event['message'])
        html= render_to_string("partial/update.html",
            {'message': event['message'], 'document_id': event['document_id'], 'student_id': event.get('student_id')}
        )
        self.send(text_data=html)
        # message= event['message']
        # document_id= event['document_id']
        # self.send(text_data=json.dumps({
        #     'message': message,
        #     'document_id': document_id
        # }))
        
