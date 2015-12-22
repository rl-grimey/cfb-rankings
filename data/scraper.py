from bs4 import BeautifulSoup
import requests, csv

rankings = []
def scraper(week):

    url = 'http://espn.go.com/college-football/rankings/_/poll/1/seasontype/2/year/2015/week/{}'.format(week)
    page = requests.get(url)
    soup = BeautifulSoup(page.text)
    table = soup.find('table')
    #print (table)

    for row in table.find_all('tr')[1:26]:
        col = row.find_all('td')

        rank = col[0].text
        team = col[1].find(text=True)
        record = col[2].text

        rankings.append({"week":week, "rank":rank, "team":team, "record":record})
        print (rankings[-1]) #sanity check

for i in range(1,16):
    scraper(i)

attrNames = ["rank", "team", "record", "week"]
with open("scraped-2015-rankings.csv", "wb") as outfile:
    writer = csv.DictWriter(outfile, fieldnames = attrNames)

    writer.writeheader()
    writer.writerows(rankings)
