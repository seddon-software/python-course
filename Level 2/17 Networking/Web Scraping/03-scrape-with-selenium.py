# Selenium requires the chromedriver to be installed on on the PATH
# use the auto installer:
#   python -m pip install chromedriver-autoinstaller

import chromedriver_autoinstaller

# Check if the current version of chromedriver exists
#   and if it doesn't exist, download it automatically,
#   then add chromedriver to path
chromedriver_autoinstaller.install()

import re, webbrowser
from bs4 import os, BeautifulSoup, Tag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# load Chrome
driver = webdriver.Chrome(executable_path="chromedriver")


def correctURLs(url):
    # add the bbc website to URL if it is missing
    base = "http://www.bbc.co.uk"
    old = 'href="/'
    new = 'href="' + base + "/"
    return url.replace(old, new)


# the pages do not load immediately so add implicit delays on all pages 
driver.implicitly_wait(5) # seconds

# open news site
driver.get("http://www.bbc.co.uk/news")

# follow a click
link = driver.find_element_by_link_text('UK')
link.click()

# now get html
html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')

# pick out spans that are tagged with class="story"
# pattern = r'(<a class="story".*?</a>)'
pattern = r'(<a[ ].*?href.*?</a>)'

pattern = re.compile(pattern, re.S)     # S modifier for multiline support
data = str(soup)
matcher = re.findall(pattern, data)     # find all anchors
# some spans have the incorrect urls which need the modifying
newMatcher = []

# ignore video links and long links (these contain embedded pictures)
for match in matcher:
    if not match.__contains__("video") and len(match) < 60:
        newMatcher.append(correctURLs(match))

# create a string of spans separated by breaks
data = "<br>".join(newMatcher)             

# save scraped info to a file
try:
    f = open("out.html", "w", encoding='utf-8')
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
    

1
