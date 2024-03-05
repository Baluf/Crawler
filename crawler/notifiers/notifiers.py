from abc import ABC, abstractmethod


class MessageNotifier(ABC):
    @abstractmethod
    def send_message(self, message, *args, **kwargs):
        pass


class SlackUserNotifier(MessageNotifier):
    USER = "at-bay"

    def send_message(self, message, *args, **kwargs):
        print(f"Sending message to Slack user {self.USER}: {message}")


class SlackChannelNotifier(MessageNotifier):
    CHANNEL = "at-bay"

    def send_message(self, message, *args, **kwargs):
        print(f"Sending message to Slack channel {self.CHANNEL}: {message}")


class EmailNotifier(MessageNotifier):
    def send_message(self, message, *args, **kwargs):
        print(f"Sending email: {message}")