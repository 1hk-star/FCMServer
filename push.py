from apscheduler.schedulers.blocking import BlockingScheduler
from feed import Feed
from settings import URL

sched = BlockingScheduler()
feed = Feed(URL)


@sched.scheduled_job('interval', seconds=1)
def getandpush():
    events = feed.get_events()


sched.start()
