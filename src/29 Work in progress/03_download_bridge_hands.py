import sys
import codecs, re
from bs4 import os, BeautifulSoup, Tag
import time

# must be able to locate chromedriver on the PATH
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 5
CHROMEDRIVER = "chromedriver-75"

def loadChromeBrowser(downloadDir):
    # driver must be on the PATH
    os.environ["PATH"] = "." + os.pathsep + os.environ["PATH"]
    options = webdriver.ChromeOptions()
    preferences = {"download.default_directory": downloadDir ,
                   "directory_upgrade"         : True,
                   "safebrowsing.enabled"      : True }
    options.add_experimental_option("prefs", preferences)
    browser = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER)
    return browser


CONGRESS = 'guildford_2015'
congress = {
    'guildford_2016'       : "http://www.bridgewebs.com/cgi-bin/bwok/bw.cgi?pid=display_rank&msec=1&sessid=789062789219227&event=20160924_1&wd=1&club=surrey",
    'guildford_2015'       : "http://www.bridgewebs.com/cgi-bin/bwok/bw.cgi?pid=display_rank&msec=1&sessid=794445377196721&event=20150926_1&wd=1&club=surrey",
    'bournemouth_2016'     : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=597598254508548&event=20160724_1&wd=1&club=dorset",
    'berks_and_bucks_2016' : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=73056454962952&event=20160618_2&wd=1&club=bbcba",
    'berks_and_bucks_2015' : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=73056454962952&event=20150620_2&wd=1&club=bbcba",
    'reading_29_sep_16'    : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=28776660500956&event=20160929_1&wd=1&club=reading",
}


def saveCongressResults():
    d = os.path.abspath("./PBNs")
    driver = loadChromeBrowser(downloadDir=d)
    # go to the congress results page
    event = congress[CONGRESS]
    driver.get(event)
    
    # the pages do not load immediately so add implicit delays on all pages 
    driver.implicitly_wait(20) # seconds
    
    # we have to click on the travellers div to get to the correct content
    ############# selector has changed since I wrote this code
    selector="#bwbox_main_right_box > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td > table > tbody > tr > td:nth-child(5) > div"
    content = driver.find_element_by_css_selector(selector)
    content.click()
    
    # download hands as PBN file
    context = driver.find_element_by_css_selector("#downloadaspbn")
    context.click()
    
    # leave enough time for download to complete
    time.sleep(5)
    driver.quit()

def getData():
    with open("PBNs/surrey_20150926_1.pbn", "r") as f:
        s = f.read()
        print(type(s))
        print(s)
        pattern = r"[[]Deal[ ](.*\n)+?"
        pattern2 = re.compile(pattern, re.MULTILINE)
        matcher = pattern2.search(s)
        print(matcher.group())

#saveCongressResults()
getData()


