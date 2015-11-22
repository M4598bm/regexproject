import google, urllib2, bs4, re

def getResult(query):
    pages = google.search(query,num=10,start=0,stop=10)

    plist = []
    for r in pages:
        plist.append(r)

    url = urllib2.urlopen(plist[0])
    page = url.read().decode('ascii')
    soup = bs4.BeautifulSoup(page)
    raw = soup.get_text(page)
    text = re.sub("[\t\n ]+",' ',raw)
    print text

getResult("penguins")
