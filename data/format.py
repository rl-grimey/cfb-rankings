import csv

rankings = {}
outList = []
f = open("scraped-2015-rankings.csv")
for row in csv.DictReader(f):
    team = row["team"]
    week = int(row["week"])

    if team in rankings:
        rankings[team][week] = row
    else:
        rankings[team] = {}
        rankings[team][week] = row

for team in rankings:
    for week in range(1,16):
        if week in rankings[team]:
            outList.append(rankings[team][week])
        else:
            rankings[team][week] = {"team":team,"rank":"", "week":week, "record":""}
            outList.append(rankings[team][week])

with open("formatted-2015-rankings.csv", "wb") as outfile:
    writer = csv.DictWriter(outfile, fieldnames = ["rank", "team", "week", "record"])
    writer.writeheader()
    writer.writerows(outList)
