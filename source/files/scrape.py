from BeautifulSoup import BeautifulSoup

def html2tsv(html, index=0):
    """Parse the index'th HTML table in ``html``.  Return table as a list of
    tab-separated ASCII table lines"""
    soup = BeautifulSoup(html)
    tables = soup.findAll('table')
    table = tables[index]
    out = []
    for row in jet_table.findAll('tr'):
        colvals = [col.text for col in row.findAll('td')]
        out.append('\t'.join(colvals))

    return out
