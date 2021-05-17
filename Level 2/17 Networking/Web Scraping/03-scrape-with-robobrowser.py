import sys
import re; re._pattern_type = re.Pattern
from robobrowser import RoboBrowser
import webbrowser
import os
from bs4 import BeautifulSoup, Tag

base = "http://www.bbc.co.uk"

def correctURL(url):
    # add the bbc website to URL if it is missing
    base = "http://www.bbc.co.uk"
    old = 'href="/'
    new = 'href="' + base + "/"
    return url.replace(old, new)

# use mechanize to scrape spans from BBC news page
browser = RoboBrowser(parser="html5lib")
browser.open(base + "/news")

link = browser.get_link(text="UK")
browser.open(base + link['href'])
soup = browser.parsed

# pick out anchors that are tagged with the story class
# tags = soup.findAll("a", "story")
tags = soup.findAll("a")
newSoup = BeautifulSoup(features="html5lib")

for tag in tags:
    # add base url if it is missing from href
    if tag['href'][0] == "/": tag['href'] = base + tag['href']
    # add tag to new soup followed by a <br>  
    newSoup.insert(0, tag)
    br = soup.new_tag("br")
    newSoup.insert(0, br)

# convert soup into a string
data = str(newSoup)

# save scraped html to a file
try:
    f = open("out.html", "w",  encoding="UTF-8")
    f.write(data)
    f.close()
except IOError as e:
    print(e)

# display local file in browser
try: 
    url = "file:///" + os.getcwd().replace("\\", '/') + "/out.html"
    webbrowser.open_new_tab(url)    
except Exception as e:
    print(e)
    


