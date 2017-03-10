import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from pushover import Client

from feed import Feed
from settings import *

from pyfcm import FCMNotification

logger = logging.getLogger()


class PushOverPush:
    def __init__(self, user_key=PUSHOVER_USER_KEY, api_key=PUSHOVER_API_KEY):
        self.client = Client(user_key, api_token=api_key)

    def send_msg(self, title, url):
        self.client.send_message(url, title=title)

    def send_messages(self, entries):
        for i in entries:
            self.send_msg(i.title, i.link)


class FCMPush:
    def __init__(self, api_key=FCM_API_KEY, user_keys=FCM_USER_ID_PATH):
        self.client = FCMNotification(api_key=api_key)
        self.user_keys = user_keys
        with open(user_keys, 'r') as f:
            self.user_ids = [i.strip() for i in f.readlines()]

    def send_msg(self, title, url):
        message_title = title
        message_body = url
        result = self.client.notify_multiple_devices(registration_ids=self.user_ids, message_title=message_title,
                                                     message_body=message_body)
        if not result[0]['success']:
            print(result)

    def send_messages(self, entries):
        with open(self.user_keys, 'r') as f:
            self.user_ids = [i.strip() for i in f.readlines()]
        for entry in entries:
            self.send_msg(entry.title, entry.link)
        logger.debug("Pushed {n} messages".format(n=len(entries)))


pusher = FCMPush()

sched = BlockingScheduler()
feed = Feed(URL)


def getandpush():
    entries = feed.get_entries()
    pusher.send_messages(entries)


if __name__ == '__main__':
    pusher = PushOverPush()
    sched.start()
