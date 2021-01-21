import sys
import codecs
from bs4 import os, BeautifulSoup, Tag

# must be able to locate chromedriver on the PATH
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
os.environ["PATH"] = "." + os.pathsep + os.environ["PATH"]

# load Chrome
driver = webdriver.Chrome(executable_path="chromedriver")

CONGRESS = 'guildford_2016'
congress = {
    'guildford_2016'       : "http://www.bridgewebs.com/cgi-bin/bwok/bw.cgi?pid=display_rank&msec=1&sessid=789062789219227&event=20160924_1&wd=1&club=surrey",
    'guildford_2015'       : "http://www.bridgewebs.com/cgi-bin/bwok/bw.cgi?pid=display_rank&msec=1&sessid=794445377196721&event=20150926_1&wd=1&club=surrey",
    'bournemouth_2016'     : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=597598254508548&event=20160724_1&wd=1&club=dorset",
    'berks_and_bucks_2016' : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=73056454962952&event=20160618_2&wd=1&club=bbcba",
    'berks_and_bucks_2015' : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=73056454962952&event=20150620_2&wd=1&club=bbcba",
    'reading_29_sep_16'    : "http://www.bridgewebs.com/cgi-bin/bwoj/bw.cgi?pid=display_rank&msec=1&sessid=28776660500956&event=20160929_1&wd=1&club=reading",
}
# go to the congress results page
event = congress[CONGRESS]
driver.get(event)

# the pages do not load immediately so add implicit delays on all pages 
driver.implicitly_wait(20) # seconds

# we have to click on the travellers div to get to the correct content
selector="#bwbox_main_right_box > tbody > tr > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2) > td > table > tbody > tr > td:nth-child(4) > div"
content = driver.find_element_by_css_selector(selector)
content.click()

# get the htlm and pass it to BeautifulSoup4
# body = driver.find_element_by_tag_name('body')
# wait until we can see travellers
text = driver.find_element_by_css_selector("#trav_r_1").text

# now get html
html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')

tables = soup.find_all("table", class_="brx_table")

def suitToUnicode(suit):
    lookup = { 'spade'   : '♠',
               'heart'   : '♥',
               'diamond' : '♦',
               'club'    : '♣' }
    return lookup[suit]

def getResult(board, lines):
    def getBid():
        bid = tds[2].getText()
        if bid == "N/A": return "VOID"
        if bid == "Passed Out": return "PO"
        if len(imgs) == 2:  # suit contract
            suit = suitToUnicode(imgs[0]['alt'])
            imgs.pop(0)
            bid = bid[0] + suit + bid[1:]
        return bid
    def getLead():
        lead = tds[4].getText()
        if lead == "": return ""
        if len(imgs) == 1:  # suit contract
            suit = suitToUnicode(imgs[0]['alt'])
            lead = lead[0] + suit + lead[1:]
        return lead
    def calculate_NS_score():
        ns = int("0" + tds[6].getText()) 
        ew = int("0" + tds[7].getText())
        return str(ns - ew)
    tds = lines.findChildren('td')
    imgs = lines.findChildren('img', alt=True)
    board = str(board)
    ns = tds[0].getText()
    ew = tds[1].getText()
    bid = getBid()
    if bid == "VOID" or bid == "PO":
        return "{},{},{},{},{},{},{},{},{},{}\n".format(
            board, ns, ew, bid, "-", "-", "-", "-", "-", "-")
    by = tds[3].getText()
    lead = getLead()
    tricks = tds[5].getText()
    score = calculate_NS_score()
    NS_pts = tds[8].getText()
    EW_pts = tds[9].getText()
    return "{},{},{},{},{},{},{},{},{},{}\n".format(
        board, ns, ew, bid, by, lead, tricks, score, NS_pts, EW_pts)

# write output to file and echo results to console
fileName = "results/" + CONGRESS + ".txt"
f = codecs.open(fileName, "w", "UTF-8")
f.write("board,NS,EW,bid,by,lead,tricks,score,NS_pts,EW_pts\n")
for board, table in enumerate(tables):
    board += 1
    results_even = table.find_all('tr', class_="brx_even_lg")
    results_odd  = table.find_all('tr', class_="brx_odd_lg")
    try:
        for result in results_even:
            out = getResult(board, result)
            print(out)
            f.write(out)
        for result in results_odd:
            out = getResult(board, result)
            print(out)
            f.write(out)
    except Exception as e:
        print(e)
        print("Problem with parsing on board {}".format(board))
        sys.exit()

f.close()
driver.quit()

