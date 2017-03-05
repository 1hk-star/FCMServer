import tornado.wsgi

from appInit import *


@app.route("/k/<key>")
def save_key(key):
    f = open('keys.txt', 'a')
    f.write(key + "\n")
    f.close()
    return 'Key saved'


if __name__ == '__main__':
    appsched.start()
    http_server = tornado.httpserver.HTTPServer(
        tornado.wsgi.WSGIContainer(app)
    )
    http_server.listen(8080, "0.0.0.0")
    print("Tornado server starting on port {}".format(8080))
    tornado.ioloop.IOLoop.instance().start()


