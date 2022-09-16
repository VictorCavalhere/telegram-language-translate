import requests
import json

class SendMessage:

    def __init__(self) -> None:
        with open('./v1/config/config.json') as f:
            self.config = json.load(f)

    def tel_send_message(self,chat_id, text):
        url = f'https://api.telegram.org/bot{self.config["TOKEN"]}/sendMessage'
        payload = {
                    'chat_id': chat_id,
                    'text': text
                    }
    
        r = requests.post(url,json=payload)
        return r