import google,urllib2,bs4,re

def getResult(query):
    pages = google.search(query,num = 10,start = 0, stop = 10)
    plist = []
    for r in pages:
        plist.append(r)
    url = urllib2.urlopen(plist[2])
    page = url.read().decode()
    soup = bs4.BeautifulSoup(page,'html.parser')
    raw = soup.get_text(page)
    text = re("[\t\n] +",' ',raw)
    print text

getResult("Penguins")
