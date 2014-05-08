# from datetime import date
# import tornado.escape
# import tornado.ioloop
# import tornado.web
# import tornado.gen
# import tornado.httpclient
 
# class VersionHandler(tornado.web.RequestHandler):
#     def get(self):
#         response = { 'version': '3.5.1',
#                      'last_build':  date.today().isoformat() }
#         self.write(response)
 
# class GetGameByIdHandler(tornado.web.RequestHandler):
#     def get(self, id):
#         response = { 'id': int(id),
#                      'name': 'Crazy Game',
#                      'release_date': date.today().isoformat() }
#         self.write(response)

# class GetFullPageAsyncHandler(tornado.web.RequestHandler):
#     @tornado.gen.coroutine
#     def get(self):
#         http_client = tornado.httpclient.AsyncHTTPClient()
#         http_response = yield http_client.fetch("http://www.drdobbs.com/web-development")
#         response = http_response.body.decode().replace(
#             "Most Recent Premium Content", "Most Recent Content")
#         self.write(response)
#         self.set_header("Content-Type", "text/html")

# application = tornado.web.Application([
#     (r"/getfullpage", GetFullPageAsyncHandler),
#     (r"/getgamebyid/([0-9]+)", GetGameByIdHandler),
#     (r"/version", VersionHandler)
# ])
 
# if __name__ == "__main__":
#     application.listen(8888)
#     tornado.ioloop.IOLoop.instance().start()