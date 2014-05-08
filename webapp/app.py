#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import options
from motorengine.connection import connect
from settings import settings
from urls import url_patterns

class TornadoBoilerplate(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)


def main():
    app = TornadoBoilerplate()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    io_loop = tornado.ioloop.IOLoop.instance()
    connect(options.mongo_db, host=options.mongo_host, port=options.mongo_port, io_loop=io_loop)
    io_loop.start()

if __name__ == "__main__":
    main()