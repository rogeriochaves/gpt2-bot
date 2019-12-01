import tornado.ioloop
import tornado.web
import os
import chat


def start(model):
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            self.finish(
                "Please call this url with a POST request, and the chat history on the body")

        def post(self):
            chat_history = self.request.body.decode("utf-8")
            reply = chat.bot_reply(model, chat_history)

            self.finish(reply)

    class HealthCheckHandler(tornado.web.RequestHandler):
        def get(self):
            self.finish('OK')

    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/healthcheck", HealthCheckHandler),
    ])
    port = os.getenv("PORT") or 8888
    app.listen(port)
    print("Server listening at http://localhost:" + str(port))
    tornado.ioloop.IOLoop.current().start()
