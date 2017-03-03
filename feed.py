import datetime

import easydict as easydict
import feedparser

URL = "http://dgu.ru/index.php?option=com_ninjarsssyndicator&feed_id=2&format=raw"
LAST_CHECKED = datetime.datetime(2017, 3, 1, 13, 8, 45)


def strtotime(s):
    return datetime.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S GMT")


def get_events():
    d = easydict.EasyDict(
        feedparser.parse(URL)
    )
    entries = d.entries
    entries = [
        {'title': e.title,
         'link': e.link,
         'published': strtotime(e.published),
         }
        for e in entries if strtotime(e.published) > LAST_CHECKED]
    return entries
