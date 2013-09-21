import web
import json
import sunlight

# Load up the api key
try:
    with open('sunlight.key') as f: sunlight.API_KEY = f.read.strip()
except IOError:
    print 'Loading key from environment'

# map up a server
render = web.template.render('templates/', base='layout')
app = web.application((
    '/',            'Index',
    '/hi',          'SayHi',
    '/legislators', 'Legislators'
), globals())

class Index:
    'Render the base index file'
    def GET(self):
        return render.index()

class SayHi:
    'Say hi to the world!'
    def GET(self):
        return 'Hey Hack Jersey!'

class Legislators:
    'List some legislators showing pulling data from the API'
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(sunlight.openstates.legislators(state="nj"))

if __name__ == '__main__':
    app.run()
