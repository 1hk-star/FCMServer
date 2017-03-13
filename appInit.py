import flask
import logging
from apscheduler.schedulers.tornado import TornadoScheduler

from push import getandpush

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
appsched = TornadoScheduler()
appsched.add_job(getandpush, 'interval', minutes=30, id='GetFeedAndPush')
logger = logging.getLogger()

