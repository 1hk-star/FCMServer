import flask
from apscheduler.schedulers.tornado import TornadoScheduler
from raven.contrib.flask import Sentry

from push import getandpush

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
appsched = TornadoScheduler()
appsched.add_job(getandpush, 'interval', minutes=1, id='GetFeedAndPush')

sentry = Sentry(app, dsn='https://47288516498c488a82ea0919ccd428f3:afb9e07f7319499b94fc6a7946d76f73@sentry.io/145010')
