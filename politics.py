import web
import json
import sunlight

# This is our router
urls = (
    '/hi',          'SayHi',
    '/legislators', 'Legislators'
)

# create a new application
app = web.application(urls, globals())

# Say hi to the world!
class SayHi:

    # We'll say hi to anyone.
    def GET(self):
        return 'Hey Hack Jersey!'

class Legislators:

    # List some legislators so we can prove we're pulling data
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(sunlight.openstates.legislators(state="nj"))

# Run the application
if __name__ == '__main__':
    app.run()
