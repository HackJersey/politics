# Helllo
import web
import json
import sunlight
import csv

# Load up the api key
try:
    with open('sunlight.key') as f: sunlight.API_KEY = f.read().strip()
except IOError:
    print 'Loading key from environment'

# A person
class Person:
    def __init__(self, row):
        self.year = row['year']
        self.name = row['name']
        self.win = row['win'] == 'W'
        self.seat = row['seat']
        self.district = row['district']
        self.rec_id = row['rec_id']
        self.entity_id = row['entity_id']

# read in the people
with open('nj_state_candidates.json') as jsonin:
    data = json.load(jsonin)
    people = [Person(entry) for entry in data if entry['win']] # skip non-people

# print the number of people
print len(people)

# map up a server
render = web.template.render('templates/', base='layout')
app = web.application((
    '/',            'Index',
    '/hi',          'SayHi',
    '/legislators', 'Legislators',
    '/people/(\d{4})/(.+?)/(.+?)', 'Filter'
), globals())

class Filter:
    'Filter the data per year, ar, and seat'
    def GET(self, year, district, seat):
        global people
        pep = [x for x in people if x.year == year]
        pep = [x for x in pep if x.district == district]
        pep = [x for x in pep if x.seat == seat]
        return json.dumps([p.__dict__ for p in pep])

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
