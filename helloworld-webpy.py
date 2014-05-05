import web
import socket

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, %s from %s!\n' % (name,socket.gethostname())

if __name__ == "__main__":
    app.run()
