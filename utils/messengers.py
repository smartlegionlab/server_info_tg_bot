# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import urllib.request
import urllib.parse
import json


class TelegramMessenger:
    def __init__(self, token):
        self.token = token
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def send_message(self, chat_id, message):
        url = f"{self.base_url}sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message
        }
        data_encoded = urllib.parse.urlencode(payload).encode('utf-8')

        req = urllib.request.Request(url, data=data_encoded, method='POST')
        req.add_header('Content-Type', 'application/x-www-form-urlencoded')

        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                return json.loads(response.read().decode('utf-8'))
            else:
                raise Exception(f"Error: {response.status} - {response.read().decode('utf-8')}")
