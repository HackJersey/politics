import web
import json
import sunlight
from influenceexplorer import InfluenceExplorer
api = InfluenceExplorer('2d657143a8b64b52b5a8d3a12df38328')

# Load up the api key
try:
    with open('sunlight.key') as f: sunlight.API_KEY = f.read.strip()
except IOError:
    print 'Loading key from environment'

# map up a server
render = web.template.render('templates/', base='layout')
app = web.application((
    '/',            'Index',
    '/candidates/',  'Candidates',
    '/candidate/(.+)',  'Candidate',
    '/legislators', 'Legislators'
), globals())

class Index:
    'Render the base index file'
    def GET(self):
        return render.index()

class Candidates:
    def GET(self):
        try:
            json_data = open('static/njcandits.json', 'r')
            data = json.load(json_data)
            json_data.close()
            web.header('Content-Type', 'application/json')
            return pprint(data)
        except:
            return ''
 
# usage: candidate/ENTITYID?CYCLE
# returns: top industry contributors for a candidate based on entity id and cycle
class Candidate:
    def GET(self, id):
    	date = web.input()
        web.header('Content-Type', 'application/json')
        return json.dumps(api.pol.industries(id, cycle=date))

class Legislators:
    'List some legislators showing pulling data from the API'
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(sunlight.openstates.legislators(state="nj"))

if __name__ == '__main__':
    app.run()
