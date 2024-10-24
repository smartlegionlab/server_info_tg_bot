# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import json
import os


class ConfigParser:
    def __init__(self, file_path):
        self.file_path = self.get_file_path(file_path)
        self.config = self.load_config()

    @staticmethod
    def get_file_path(file_name):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        return os.path.join(project_root, file_name)

    def load_config(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                config_json = file.read()
                return json.loads(config_json)
        except FileNotFoundError:
            raise Exception(f"File {self.file_path} not found.")
        except json.JSONDecodeError as e:
            raise Exception(f"JSON decoding error: {e}")

    def get_token(self):
        return self.config.get("token", "")

    def get_admins(self):
        return self.config.get("admins", [])

    def get_admin_chat_ids(self):
        return self.get_admins()
