async def receive(self, text_data):
    data = json.loads(text_data)
    if data.get('type') == 'reaction':
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_reaction',
                'emoji': data['emoji']
            }
        )
    else:
        # existing message handling
        ...
        
async def chat_reaction(self, event):
    emoji = event['emoji']
    await self.send(text_data=json.dumps({
        'reaction': emoji
    }))
