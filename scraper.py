import scraperwiki
from lxml import etree
import sqlite3

root = etree.fromstring(scraperwiki.scrape('http://www.europarl.europa.eu/meps/en/xml.html?country=DE'))

members = []

for member in root:

    member = {
        'id': member.find('id').text,
        'name': member.find('fullName').text.title(),
        'area_id': 'DE',
        'area_type_description': 'Country',
        'national_party': member.find('nationalPoliticalGroup').text,
        'ep_group': member.find('politicalGroup').text
    }

    members.append(member)

try:
    scraperwiki.sqlite.execute('DELETE FROM data')
except sqlite3.OperationalError:
    pass
scraperwiki.sqlite.save(
    unique_keys=['id'],
    data=members)
