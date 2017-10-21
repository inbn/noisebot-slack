#!env/bin/python

from slackclient import SlackClient
from importlib import import_module
from time import sleep
import config
import os


class Bot():
    def __init__(self, config):

        self.config = config
        self.connect()

    def connect(self):
        """ connect to slack """

        self.sc = SlackClient(self.config.slack["api_key"])
        self.users = self.sc.api_call("users.list")
        self.channel = "#general"
        self.message_text = "It’s noisy in here! :mega:"

        self.bot_user = self.get_user_id_by_name(
            self.config.slack["bot_name"])

        self.sc.api_call(
            "chat.postMessage",
            channel=self.channel,
            text=self.message_text,
            as_user=self.bot_user
        )

    def get_user_id_by_name(self, user_name):
        for user in self.users["members"]:
            if user["name"] == user_name:
                return user["id"]

noisebot = Bot(config)
