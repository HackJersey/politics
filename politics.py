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
        self.year = row['year']
        self.name = row['name']
        self.win = row['win'] == 'W'
        self.seat = row['seat']
        self.district = row['district']
        self.rec_id = row['rec_id']
        self.entity_id = 'f0bc8ebfa30545778d012ecb984882eb' # row['entity_id']

    # get the top contributors for these
    def top_contribs(self):
        return api.pol.industries(self.entity_id, cycle=self.year)

    # Our output format
    def nice_data(self):
        d = {}
        d['top_contribs'] = self.top_contribs()
        d['name'] = self.name
        d['win'] = self.win
        return d

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
    '/about',       'About',
    '/candidates/',  'Candidates',
    '/candidate/(.+)',  'Candidate',
    '/legislators', 'Legislators',
    '/years',       'Years',
    '/races/(.+)', 'Races',
    '/hi',          'SayHi',
    '/people/(\d{4})/(.+?)/(.+?)', 'Filter'
), globals())

class Races:
    'Races for a year'
    def GET(self, year):
        global people
        pep = [x for x in people if x.year == year]
        return json.dumps(list(set([p.district for p in pep])))

class Years:
    'Filter the data per year, ar, and seat'
    def GET(self):
        global people
        return json.dumps(list(set([p.year for p in people])))

class Filter:
    'Filter the data per year, ar, and seat'
    def GET(self, year, district, seat):
        global people
        pep = people
        pep = [x for x in people if x.year == year]
        if district == 'gov':
            pep = [x for x in pep if x.seat is None]
        else:
            pep = [x for x in pep if x.district == district]
            pep = [x for x in pep if x.seat == seat]
        return json.dumps([p.nice_data() for p in pep])

class Index:
    'Render the base index file'
    def GET(self):
        return render.index()

class About:
    'Render the about page'
    def GET(self):
        return render.about()

class Legislators:
    'List some legislators showing pulling data from the API'
    def GET(self):
        web.header('Content-Type', 'application/json')
        return json.dumps(sunlight.openstates.legislators(state="nj"))

if __name__ == '__main__':
    app.run()
