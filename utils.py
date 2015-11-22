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
    if("who" in query):
        """
        finds all text with capitals for 2 consecutive words
        """
        text = re.findall("[A-Z][a-z] + [A-Z][a-z]+",raw)
    elif("where" in query):
        """
        finds all text with one capital
        """
        text = re.findall("[A-Z][a-z]+",raw)
    else:
        """
        not sure how to do when yet
        """
        text = re.findall(" ");
    dictionary = {}
    for result in text:
        """
        if the result has been found before, add 1 to number of occurence
        """
        if name in dictionary.keys():
            dictionary[result] += 1
        """
        if the result hasn't been found before, set the occurence equal to one
        """
        else:
            dictionary[result] = 1
    """
    testing purposes
    """
    for key in dictionary.keys():
        print "%s:%d" % (key,dictionary[key])
    return findResult(dictionary)
        
def findResult(dictionary):
    result = dictionary.keys()[0]
    for key in dictionary.keys():
        if(key.get() > result.get()):
            result = key
    return result

#getResult("Penguin")
findResult({"a":1,"b":2,"c":3})
