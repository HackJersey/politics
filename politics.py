# Helllo 
import web
import json
import sunlight

import csv

from influenceexplorer import InfluenceExplorer
api = InfluenceExplorer('2d657143a8b64b52b5a8d3a12df38328')


# Load up the api key
try:
    with open('sunlight.key') as f: sunlight.API_KEY = f.read().strip()
except IOError:
    print 'Loading key from environment'

# A person
class Person:
    def __init__(self, row):
        self.year = row[0]
        self.name = row[2]
        self.win = row[3]
        self.ar = row[4]
        self.seat = row[5]
    def nice_hash(self):
        d = {}
        d['win'] = self.win == 'W'
        d['name'] = self.name
        return d

# read in the people
with open('nj_candidates_more.tsv') as tsvin:
    tsv = csv.reader(tsvin, delimiter='\t')
    people = [Person(row) for row in tsv if len(row) > 3]

# print the number of people
print len(people)

# map up a server
render = web.template.render('templates/', base='layout')
app = web.application((
    '/',            'Index',
    '/candidates/',  'Candidates',
    '/candidate/(.+)',  'Candidate',
    '/legislators', 'Legislators',
    '/hi',          'SayHi',
    '/people/(\d{4})/(.+?)/(.+?)', 'Filter'
), globals())

class Filter:
    'Filter the data per year, ar, and seat'
    def GET(self, year, ar, seat):
        global people
        pep = [x for x in people if x.year == year]
        pep = [x for x in pep if x.ar == ar]
        pep = [x for x in pep if x.seat == seat]
        return json.dumps([p.nice_hash() for p in pep])

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
