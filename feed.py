import datetime

import easydict as easydict
import feedparser
import requests
from bs4 import BeautifulSoup


def strtotime(s):
    return datetime.datetime.strptime(s, "%a, %d %b %Y %H:%M:%S GMT")


class RssFeed:
    def __init__(self, url):
        self.url = url

    LAST_CHECKED = datetime.datetime(2017, 3, 1, 13, 8, 45)

    def get_entries(self):
        d = easydict.EasyDict(
            feedparser.parse(self.url)
        )
        entries = d.entries
        entries = [
            easydict.EasyDict({'title': e.title,
                               'link': e.link,
                               'published': strtotime(e.published),
                               })
            for e in entries if strtotime(e.published) > self.LAST_CHECKED]
        self.LAST_CHECKED = strtotime(d.feed.updated)
        return entries


class MFeed:
    url = "http://math.dgu.ru/news.aspx"

    LAST_CHECKED = datetime.datetime(2017, 3, 1, 13, 8, 45)

    def __str_to_date(self, datestr):
        d, m, y = map(int, datestr.split("."))
        return datetime.datetime(y, m, d)

    def get_entries(self):
        soup = BeautifulSoup(requests.get(self.url).content, 'html.parser')
        news = soup.find(id="ContentPlaceHolder1_news1_newsListView_itemPlaceholderContainer")
        news = [n for n in news.children if len(n) > 1]
        entries = [
            easydict.EasyDict({
                'title': n.em.span.text.strip(),
                'url': self.url,
                'published': n.span.text,
            })
            for n in news
            if self.__str_to_date(n.span.text) > self.LAST_CHECKED
        ]
        if len(entries) > 0:
            self.LAST_CHECKED = self.__str_to_date(entries[0].published)
        return entries
