import tornado.ioloop
import tornado.web
import os


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        if not self.get_arguments("chat_history"):
            self.set_status(
                400, reason='Please send a ?chat_history GET param, with some string like "- John Doe: Hello"')
            self.write_error(400)
            return
        message = self.get_arguments("chat_history")[0]
        reply = "hello"

        self.finish(reply)


class HealthCheckHandler(tornado.web.RequestHandler):
    def get(self):
        self.finish('OK')


def start():
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/healthcheck", HealthCheckHandler),
    ])
    port = os.getenv("PORT") or 8888
    app.listen(port)
    print("Server listening at http://localhost:" + str(port))
    tornado.ioloop.IOLoop.current().start()
