############################################################
#
#    sendmail
#
############################################################

import smtplib, ssl
import getpass

password = getpass.getpass('Password: ')
sender_email = "seddon_software@btinternet.com"
receiver_email = "ljs21@btinternet.com"
smtp_server = 'mail.btinternet.com'
message = """\
Subject: Sending email via a script

This message is sent from Chris Seddon to you.
"""
port = 465  # For SSL
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(f"Chris Seddon <seddon_software@btinternet.com>", receiver_email, message)
except Exception as e:
    print(e)



