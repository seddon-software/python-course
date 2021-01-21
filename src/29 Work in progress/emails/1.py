import mailbox, re
from bs4 import os, BeautifulSoup, Tag

pythonMBox =  mailbox.mbox('/Users/seddon/Library/Thunderbird/Profiles/yr6sspxv.default/Mail/pop3.keme.co-6.uk/Inbox.sbd/Python')

#import urllib.parse, sys
from email.header import decode_header

def decodePart(n, part):
    body = part.get_payload(decode=True)
    type = part.get_content_type()
    if body:
# soup = BeautifulSoup(html, 'html5lib')
# text = driver.find_element_by_css_selector("#x0_0").text
# table = soup.find("table", class_="outer")
        soup = BeautifulSoup(body.decode(), 'html.parser')
        a = soup.find_all("a")
        for link in a:
            text = link.get_text()
            if re.search("async", text, re.I):
                print(f"{text}")
            
    
    
for message in pythonMBox:
    m = message['subject']
#     f = message['from']
#     t = message['to']
#     d = message['date']
    print(decode_header(m)[0][0].decode(), end="; ")    
#     print(decode_header(f)[0][0].decode(), end="; ")    
#     print(decode_header(t)[0][0], end="; ")
#     print(" ".join(d.split()[1:4])) 
    print()
    
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.is_multipart():
                        decodePart(1, part)
                    else:
                        decodePart(2, part)
            else:
                decodePart(3, part)
    elif message.get_content_type() == 'text/plain':
        decodePart(4, message)
    else:
        decodePart(5, message)
    #sys.exit()
