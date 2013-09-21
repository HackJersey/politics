import web

# This is our router
urls = (
    '/(.*)', 'politics'
)

# create a new application
app = web.application(urls, globals())

# And this is our app
class politics:
    def GET(self, name):
        return 'Hey Hack Jersey!'

# Run the application
if __name__ == '__main__':
    app.run()
