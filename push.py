from apscheduler.schedulers.blocking import BlockingScheduler
from feed import Feed

sched = BlockingScheduler()
feed = Feed("http://dgu.ru/index.php?option=com_ninjarsssyndicator&feed_id=2&format=raw")


@sched.scheduled_job('interval', seconds=1)
def getandpush():
    events = feed.get_events()


sched.start()
