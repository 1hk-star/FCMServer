import datetime

import easydict as easydict
import feedparser

class Feed:
    def __init__(self, url):
        self.url = url

    def __strtotime(self, s):
        return datetime.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S GMT")

    LAST_CHECKED = datetime.datetime(1017, 3, 1, 13, 8, 45)

    def get_events(self):
        d = easydict.EasyDict(
            feedparser.parse(self.url)
        )
        entries = d.entries
        entries = [
            {'title': e.title,
             'link': e.link,
             'published': self.__strtotime(e.published),
             }
            for e in entries if self.__strtotime(e.published) > self.LAST_CHECKED]
        self.LAST_CHECKED = self.__strtotime(d.feed.updated)
        return entries
