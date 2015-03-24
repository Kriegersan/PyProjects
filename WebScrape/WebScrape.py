__author__ = 'knelson'
import urllib2
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://www.bcsfootball.org').read())

for row in soup('table', ({'class': 'mod-data'}))[0].tbody('tr'):
    tds = row('td')
    print tds[0].string. tds[1].string