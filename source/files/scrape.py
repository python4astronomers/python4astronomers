from BeautifulSoup import BeautifulSoup
import urllib2
import asciitable

url = 'http://hea-www.harvard.edu/XJET/'
page = urllib2.urlopen(url).read()

soup = BeautifulSoup(page)

tables = soup.findAll('table')
jettable = tables[1]

out = []
for row in jettable.findAll('tr'):
    colvals = []
    for col in row.findAll('td'):
        colvals.append(col.text)
    out.append('\t'.join(colvals))

dat = asciitable.read(out)
