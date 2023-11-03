from channels.generic.websocket import JsonWebsocketConsumer


class RolePlayingRoomConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0  # 웹소켓 접속마다 따로 유지되는 변수

    def receive_json(self, content, **kwargs):
        self.count += 1
        content["count"] = self.count
        self.send_json(content)  # Echo 응답.
