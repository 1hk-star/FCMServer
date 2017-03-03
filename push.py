from apscheduler.schedulers.blocking import BlockingScheduler
from pushover import Client

from feed import Feed
from settings import *

from pyfcm import FCMNotification

push_service = FCMNotification(api_key=GCM_API_KEY)


class PushOverPush:
    def __init__(self, user_key=PUSHOVER_USER_KEY, api_key=PUSHOVER_API_KEY):
        self.client = Client(user_key, api_token=api_key)

    def send_msg(self, title, url):
        self.client.send_message(url, title=title)

    def send_messages(self, entries):
        for i in entries:
            self.send_msg(i.title, i.link)


#class PushOverPush:
#    pass


sched = BlockingScheduler()
feed = Feed(URL)


@sched.scheduled_job('interval', seconds=1)
def getandpush():
    entries = feed.get_entries()


sched.start()
