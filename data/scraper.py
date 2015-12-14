from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

rankings = {}
counter = 0
# for i in range(1,16):

url = 'http://espn.go.com/college-football/rankings/_/poll/seasontype/2/year/2015/week/1'
page = urlopen(url).read()
soup = BeautifulSoup(page)

table = soup.find('table')
for row in table.find_all('tr')[1:26]:
    col = row.find_all('td')

    rank = col[0].text
    team = col[1].text
    record = col[2].text

    rankings[counter] = {"rank":rank, "team":team, "record":record}
    counter += 1

print (rankings)
