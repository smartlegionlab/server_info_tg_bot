# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import os
import sys
import time

from utils.config import Config
from utils.informers import IpInformer
from utils.messengers import TelegramMessenger
from utils.parsers import ConfigParser
from utils.printers import SmartPrinter


class AppManager:
    def __init__(self):
        self.printer = SmartPrinter()
        self.config = Config()
        self.parser = ConfigParser('config.json')
        self.messenger = None
        self.informer = IpInformer()

    def show_logo(self):
        self.printer.show_head(text=self.config.app_name)

    def show_footer(self):
        self.printer.show_footer(
            url=self.config.github_url,
            copyright_=self.config.info
        )

    def run(self):
        self.show_logo()

        token = self.parser.get_token()
        if not token:
            self.exit_app(
                message='Token is missing',
            )

        self.messenger = TelegramMessenger(
            token=token,
        )

        admins = self.parser.get_admins()
        if not admins:
            self.exit_app(
                message='Admin is missing',
            )

        local_ip = self.informer.get_local_ip()
        if local_ip is None:
            self.exit_app(
                message='Local IP is missing',
            )

        print('Waiting 30sec ...')
        time.sleep(30)
        user_login = os.getlogin()
        local_ip_info = f"Local IP: {local_ip}"
        print('Local IP received')
        user_info = f"User: {user_login}"
        print('User name received')
        command_info = f"Command: ssh {user_login}@{local_ip}"
        print('Message generated')

        message = f"{self.config.app_name}\n\n{user_info}\n{local_ip_info}\n{command_info}"

        self.printer.print_center(text="Sending information:")

        for admin in admins:
            self.messenger.send_message(admin, message)
            print(f"Message send to {self.mask_admin_chat_id(admin)} [OK]")

        self.printer.show_footer(
            url=self.config.github_url,
            copyright_=self.config.info
        )

    @staticmethod
    def mask_admin_chat_id(chat_id):
        if len(chat_id) > 4:
            masked_admin = chat_id[:2] + '*' * (len(chat_id) - 4) + chat_id[-2:]
        else:
            masked_admin = chat_id
        return masked_admin

    def exit_app(self, message):
        self.printer.print_framed(message)
        sys.exit(0)
