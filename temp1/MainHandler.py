import tornado.web
import textwrap


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument("text")
        width = self.get_argument("width", 40)
        self.write(textwrap.fill(text, width))
        pass


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/wrap", WrapHandler)
])

if __name__ == "__main__":
    print "start routing..."
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
