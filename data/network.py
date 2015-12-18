import csv, pprint

rankings = {}
outList = []
f = open("2015-rankings.csv")
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
            continue
        else:
            rankings[team][week] = {"team":team,"rank":"", "week":week, "record":""}
