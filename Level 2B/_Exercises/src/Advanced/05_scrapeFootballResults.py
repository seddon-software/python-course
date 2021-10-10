'''
This web scraping program will extract all the results for the Football Premiership season 2014-5
and produce a table that looks like:
 
Arsenal                   5–0  3–0  0–0  2–1  2–0  2–2  2–1  4–1  2–2  1–2  4–1  2–1  1–0  3–0  0–0  0–1  1–1  4–1  3–0      
Aston Villa          0–3       0–1  1–2  0–0  3–2  2–1  2–1  0–2  0–2  1–1  0–0  3–3  1–1  1–2  0–0  0–1  1–2  2–1  1–0      
Burnley              0–1  1–1       1–3  2–3  1–3  1–0  0–1  0–1  1–0  0–0  1–1  2–1  1–0  0–0  0–0  0–1  0–0  2–2  1–3      
Chelsea              2–0  3–0  1–1       1–0  1–0  2–0  2–0  1–1  1–1  1–0  2–0  2–1  1–1  2–1  3–1  4–2  3–0  2–0  2–0      
Crystal Palace       1–2  0–1  0–0  1–2       0–1  0–2  2–0  3–1  2–1  1–2  1–1  3–1  1–3  1–1  1–3  1–0  2–1  0–2  1–3      
Everton              2–2  3–0  1–0  3–6  2–3       1–1  2–2  0–0  1–1  3–0  3–0  3–1  1–0  0–1  0–2  0–0  0–1  0–0  2–1      
Hull City            1–3  2–0  0–1  2–3  2–0  2–0       0–1  1–0  2–4  0–0  0–3  2–1  0–1  1–1  1–1  0–1  1–2  0–0  2–2      
Leicester City       1–1  1–0  2–2  1–3  0–1  2–2  0–0       1–3  0–1  5–3  3–0  5–1  2–0  0–1  0–0  2–0  1–2  0–1  2–1      
Liverpool            2–2  0–1  2–0  1–2  1–3  1–1  0–0  2–2       2–1  1–2  2–0  2–1  2–1  1–0  0–0  4–1  3–2  2–1  2–0      
Manchester City      0–2  3–2  2–2  1–1  3–0  1–0  1–1  2–0  3–1       1–0  5–0  6–0  2–0  0–1  3–2  2–1  4–1  3–0  2–0      
Manchester United    1–1  3–1  3–1  1–1  1–0  2–1  3–0  3–1  3–0  4–2       3–1  4–0  0–1  2–1  2–0  1–2  3–0  0–1  2–1      
Newcastle United     1–2  1–0  3–3  2–1  3–3  3–2  2–2  1–0  1–0  0–2  0–1       1–0  1–2  1–1  0–1  2–3  1–3  1–1  2–0      
Queens Park Rangers  1–2  2–0  2–0  0–1  0–0  1–2  0–1  3–2  2–3  2–2  0–2  2–1       0–1  2–2  1–0  1–1  1–2  3–2  0–0      
Southampton          2–0  6–1  2–0  1–1  1–0  3–0  2–0  2–0  0–2  0–3  1–2  4–0  2–1       1–0  8–0  0–1  2–2  0–0  0–0      
Stoke City           3–2  0–1  1–2  0–2  1–2  2–0  1–0  0–1  6–1  1–4  1–1  1–0  3–1  2–1       1–1  2–1  3–0  2–0  2–2      
Sunderland           0–2  0–4  2–0  0–0  1–4  1–1  1–3  0–0  0–1  1–4  1–1  1–0  0–2  2–1  3–1       0–0  2–2  0–0  1–1      
Swansea City         2–1  1–0  1–0  0–5  1–1  1–1  3–1  2–0  0–1  2–4  2–1  2–2  2–0  0–1  2–0  1–1       1–2  3–0  1–1      
Tottenham Hotspur    2–1  0–1  2–1  5–3  0–0  2–1  2–0  4–3  0–3  0–1  0–0  1–2  4–0  1–0  1–2  2–1  3–2       0–1  2–2      
West Bromwich Albion 0–1  1–0  4–0  3–0  2–2  0–2  1–0  2–3  0–0  1–3  2–2  0–2  1–4  1–0  1–0  2–2  2–0  0–3       1–2      
West Ham United      1–2  0–0  1–0  0–1  1–3  1–2  3–0  2–0  3–1  2–1  1–1  1–0  2–0  1–3  1–1  1–0  3–1  0–1  1–1           
'''

import mechanize
from bs4 import BeautifulSoup

def findAllRowsInResultsTable(soup):
	table = soup.find("table", {"class":"wikitable plainrowheaders"})
	trs = table.find_all("tr")
	trs.pop(0)		# headings
	return trs

def getSoup(url):
	br = mechanize.Browser()
	br.open(url)
	data = br.response().read()
	soup = BeautifulSoup(data, "lxml")
	return soup

# def extractTeam(text):
# 	'the teams have a strange format with an ! separating two copies of the team names'
# 	fields = text.split('!')
# 	return fields[1]

url="https://en.wikipedia.org/wiki/2018-19_Premier_League#Result_table"
teams = [ ]
scores = [ ]
soup = getSoup(url)
trs = findAllRowsInResultsTable(soup)
for tr in trs:
	row =  tr.find_all(text=True)
	entry = [str(col) for col in list(row) if str(col) != "\n"]
	team = entry.pop(0)
	teams.append( team )
	teamScores = [ ]
	for col in entry:
		teamScores.append(col.strip())
	scores.append(teamScores)

league = zip(teams, scores)

for team, results in league:
	print(f"{team:24s}", end=" ")
	for state_centroid in results:
		print(f"{state_centroid:4s}", end=" ")
	print() 


