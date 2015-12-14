from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

rankings = {}
counter = 0
for i in range(1,16):
    week = i

    url = 'http://espn.go.com/college-football/rankings/_/poll/seasontype/2/year/2015/week/{}'.format(week)
    page = urlopen(url).read()
    soup = BeautifulSoup(page)

    table = soup.find('table')
    for row in table.find_all('tr')[1:26]:
        col = row.find_all('td')

        rank = col[0].text
        team = col[1].find(text=True)
        record = col[2].text

        rankings[counter] = {"week":week, "rank":rank, "team":team, "record":record}
        counter += 1

with open("2015-rankings.csv", "wb") as outfile:
    attrNames = ["rank", "team", "record", "week"]
    writer = csv.DictWriter(outfile, fieldnames = attrNames)

    writer.writeheader()
    for row in rankings:
        writer.writerow(rankings[row])
