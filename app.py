import argparse

import tornado.wsgi
import tornado.httpserver
import tornado.ioloop

from appInit import *


@app.route("/k/<key>")
def save_key(key):
    f = open('keys.txt', 'a')
    f.write(key + "\n")
    f.close()
    return 'Key saved'


def run(port=8080):
    appsched.start()
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app)
    )
    http_server.listen(8080, "0.0.0.0")
    print("Tornado server starting on port {}".format(port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a task')
    parser.add_argument('--port', dest='port',
                        help='Port to run on',
                        default=8080, type=int)
    args = parser.parse_args()
    run(args.port)
