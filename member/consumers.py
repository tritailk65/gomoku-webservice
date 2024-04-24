import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Có thể tạo nhiều phòng chơi ở đây
        self.room_group_name='test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connect_established',
            'message': 'You are now connected!'
        }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'handle_send',
                'message': text_data_json
            }
        )
    
    def handle_send(self, event):
        data = event['message']
        player = data["player"]
        position = data["position"]
        row = position["row"]
        column = position["column"]
        self.send(text_data=json.dumps({
            'type': 'move',
            'player': player,
            'position':{
                "row": row,
                "column": column
            }
        }))

