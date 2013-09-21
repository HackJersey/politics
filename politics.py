import web
import json
import sunlight

app = web.application((
    '/hi',          'SayHi',
    '/legislators', 'Legislators'
), globals())

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
