import web

# This is our router
urls = (
    '/hi', 'politics.SayHi'
)

# create a new application
app = web.application(urls, globals())

# Say hi to the world!
class SayHi:

    # We'll say hi to anyone.
    def GET(self):
        return 'Hey Hack Jersey!'

# Run the application
if __name__ == '__main__':
    app.run()
