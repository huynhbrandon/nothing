#! python3

# downloads highest grossing franchise information

import urllib.request, bs4, csv
#request lib to download the page, bs4 to look at things cooler, csv to write to excel

f = open("dataoutput2.csv", "w", newline = '') #opens an output file to write to
writer = csv.writer(f)          

url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_video_game_franchises"

print('Downloading page...')

res = urllib.request.urlopen(url) #downloads the page
 # check that it works

soupdata = bs4.BeautifulSoup(res.read(), 'lxml') #parsing

table = soupdata.find('table', {"class":"wikitable sortable"})

rows = table.findAll('tr')

for tr in rows:
        cols = tr.findAll(recursive = False)
        cols = [ele.text.strip() for ele in cols]

        writer.writerow(cols)
        f.flush()
        print(cols)
f.close()
