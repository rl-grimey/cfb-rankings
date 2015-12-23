data/formatted-2015-rankings.csv: data/scraped-2015-rankings.csv
	python data/format.py
	mv *.csv data
	python -m SimpleHTTPServer 8888 &

data/scraped-2015-rankings.csv: data/scraper.py
	python data/scraper.py
