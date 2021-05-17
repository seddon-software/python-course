import os, email, urllib
from bs4 import os, BeautifulSoup, Tag

# os.system("ls /Users/seddon/Library/Thunderbird/Profiles/yr6sspxv.default/Mail/pop3.keme.co-6.uk/Inbox/Mail")

myMailbox = "/Users/seddon/Library/Thunderbird/Profiles/yr6sspxv.default/Mail/pop3.keme.co-6.uk/Inbox.sbd/Python"
import mailbox

mbox = mailbox.mbox(myMailbox)
import urllib.parse
import email.header
from email.message import Message

for message in mbox:
    def getbody(message): #getting plain text 'email body'
        body = None
        if message.is_multipart():
            for part in message.walk():
                if part.is_multipart():
                    for subpart in part.walk():
                        if subpart.get_content_type() == 'text/plain':
                            body = subpart.get_payload(decode=False)
                elif part.get_content_type() == 'text/plain':
                    body = part.get_payload(decode=False)
        elif message.get_content_type() == 'text/plain':
            body = message.get_payload(decode=False)
        return body
    html = getbody(message)
    for line in html.split("\n"):
        if "Welcome to issue" in line: print(line[:38])
        if "Djang" in line: print(line)
