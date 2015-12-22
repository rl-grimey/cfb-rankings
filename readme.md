# ReadMe & ToDo

This repo holds my work for the 2015 College Football Rankings. Football isn't something I usually follow, but it's popular and has fairly complete data. Contained within...

  - ESPN scraping & formatting python scripts
  - D3 visualizations. Specifically a bump chart of the NCAA CFB rankings, week by week.
  - Black magic

![Example gif of visualization](https://raw.githubusercontent.com/ryan-p-larson/rankings/master/examples/example.gif)


### Installation

The repo comes with a makefile to prep the data and then start a local server. You will need the BeautifulSoup and Requests Python modules for the scraping portion. The visualization will use D3.js and is included within the repo. 

```sh
$ git clone https://github.com/ryan-p-larson/rankings.git
$ cd rankings
$ make
```
Thats's it! Open up localhost:8888/index.html to see the bump chart.

### Todos

 - [x] Write python script to add null weeks to the data sets. Ex: D3 will create a line from a Week 6 ranking to a Week 9 ranking, even if the team wasn't ranked in 7 & 8.
 - [x] Show all teams, not just the teams from week to week.
 - [  ] Analytics questions answered! Ex: 'Who dropped/gained the most?', 'Greatest overall season trend?', and 'What were the biggest games affecting team rankings?'
 - [x] Styling, more graphs, automating, etc

License
----

MIT
**Free Software, Hell Yeah!**
