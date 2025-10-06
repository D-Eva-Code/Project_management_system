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
        if user.is_authenticated and user.role == "supervisor":
            self.group_name= f"supervisor_{user.id}"
            print("🧠 Supervisor WebSocket joined group:", self.group_name)


            async_to_sync(self.channel_layer.group_add)(
                self.group_name, self.channel_name
            )
            self.accept()
        
    def disconnect(self, close_code):
        if hasattr(self, "group_name"):
            async_to_sync(self.channel_layer.group_discard)(
                self.group_name, self.channel_name
            )

    def file_uploaded(self, event):
        print("📨 Consumer received event:", event)
        # self.send(text_data=event['message'])
        html= render_to_string("partial/update.html",
            {'message': event['message'], 'owner_id': event['owner_id']}
        )
        self.send(text_data=html)
        # self.send(text_data=json.dumps({
        #     'html': html,
        #     'owner_id': event['owner_id']
        # }))
        # message= event['message']
        # document_id= event['document_id']
        # self.send(text_data=json.dumps({
        #     'message': message,
        #     'document_id': document_id
        # }))
        
