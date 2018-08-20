#! python3

# downloads highest grossing franchise information

import urllib.request, bs4, csv
#request lib to download the page, bs4 to look at things cooler, csv to write to excel

f = open("billionaires.csv", "w", newline = '') #opens an output file to write to
writer = csv.writer(f)          

url = "https://www.forbes.com/billionaires/list/"

print('Downloading page...')

res = urllib.request.urlopen(url) #downloads the page
 # check that it works

soupdata = bs4.BeautifulSoup(res.read(), 'lxml') #parsing

#table = soupdata.find('table', {"id":"the_list"})

table2 = soupdata.find('div' , {"id":"real_time"})

#print(table2)

square = table2.findAll('li' , {"class" : ["plus", "minus"]})

#print(square)





#print(rows)


for li in square:
        cols = li.findAll(recursive = False)
        cols = [ele.text.strip() for ele in cols]

        writer.writerow(cols)
        f.flush()
        print(cols)

f.close()
