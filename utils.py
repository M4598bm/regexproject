import google, urllib2, bs4, re

def getResult(query):
    pages = google.search(query,num=10,start=0,stop=10)

    plist = []
    for r in pages:
        plist.append(r)

    url = urllib2.urlopen(plist[0])
    page = url.read()
    soup = bs4.BeautifulSoup(page)
    raw = soup.get_text(page)
    text = []
    if("who" in query):
        """
        finds all text with capitals for 2 consecutive words
        """
        text = re.findall("[A-Z][a-z]+ [A-Z][a-z]+",raw)
        person = makedict(text)
        return findResult(person)
    elif("where" in query):
        """
        finds all text with one capital
        """
        text = re.findall("[A-Z][a-z]+",raw)
        place = makedict(text)
        return findResult(place)
    else:
        """
        makes 3 dictionaries for month,day,year
        """
        text = re.findall("[A-z][a-z]+",raw)
        text2 = re.findall("[0-3]?[[0-9]",raw)
        text3 = re.findall("[0-2]?[0-9]{3}",raw)
        month = makedict(text)
        day = makedict(text2)
        year = makedict(text3)
        return findResult(month) + "," +  findResult(day) + "," + findResult(year)
        
"""
makes a dictionary for all the search results
"""
def makedict(list):
    dictionary = {}
    for item in list:
        """
        if the item has been found before, add 1 to number of occurence
        """
        if item in dictionary.keys():
            dictionary[item] += 1
            """
            if the item hasn't been found before, set the occurence equal to one
            """
        else:
            dictionary[item] = 1
        
        """
        testing purposes
        """
        for key in dictionary.keys():
            print "%s:%d" % (key,dictionary[key])
    return dictionary

def findResult(dictionary):
    result = dictionary.keys()[0]
    for key in dictionary.keys():
        if(key.get() > result.get()):
            result = key
    return result

#getResult("Penguin")
print findResult({"a":1,"b":2,"c":3})
