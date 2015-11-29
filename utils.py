import google, urllib2, bs4, re

def getResult(query):
    low = query.lower()
    if("where" not in low and "who" not in low and "when" not in low): 
        return "Ask an appropriate question please"
    
    """
        
    """
    pages = google.search(query,num=10,start=0,stop=5)

    plist = []
    text = []
    """
    These two lists below are only used for dates
    """
    text2 = []
    text3 =[]
    
    for r in pages:
        plist.append(r)

    i = 0
    while i < 5:
        try:
            url = urllib2.urlopen(plist[i])
            page = url.read().decode('utf-8')
            soup = bs4.BeautifulSoup(page,"html.parser")
            raw = soup.get_text(page)
        except:
            """
            when the webpage is inaccesible, return nothing
            """
            raw = ""
        if("who" in low):
            """
            finds all text with capitals for 2 consecutive words
            """
            text += re.findall("[A-Z][a-z]+ [A-Z][a-z]+",raw[100:500])
            
        elif("where" in low):
            """
            finds all places with the format City, Country
            """
            text += re.findall("[A-Z][a-z]+,[ ]?[A-Z][a-z]+",raw[100:1000])
            
        else:
            """
            makes 3 dictionaries for month,day,year
            """
            text += re.findall("January|February|March|April|May|June|July|August|September|October|November|December",raw[100:1000])
            text2 += re.findall("[0-3]?[0-9]",raw[100:1000])
            text3 += re.findall("[0-2][0-9]{3}",raw[100:1000])
            
        i += 1
    if("when" not in low):
        dictionary = makedict(text)
        if(dictionary != {}):
            return findResult(dictionary)
        else:
            return "No results found"
    else:
        month = findResult(makedict(text))
        day = findResult(makedict(text2))
        year = findResult(makedict(text3))
        
        return month + "," + day + "," + year
    
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
    #for key in dictionary.keys():
        #print "%s:%d" % (key,dictionary[key])
    return dictionary

"""
finds the item that occurs the most in the dictionary
"""
def findResult(dictionary):
    if dictionary == {}:
        return " "
    result = dictionary.keys()[0]
    for key in dictionary.keys():
        if(dictionary[key] > dictionary[result]):
            result = key
    return result

