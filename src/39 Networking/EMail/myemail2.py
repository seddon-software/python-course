############################################################
#
#    main.py
#
############################################################

import smtplib
server = smtplib.SMTP('mail.guardedhost.com')
server = smtplib.SMTP('mail.btinternet.com')

USER = "seddon_software@btinternet.com"
#Next, log in to the server
server.login(USER, PASSWORD)

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail(USER, USER, msg)