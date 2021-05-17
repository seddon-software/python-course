############################################################
#
#    main.py
#
############################################################

import smtplib
server = smtplib.SMTP('mail.guardedhost.com')


#Next, log in to the server
server.login("surveyor@highlandsnegotiations.com", "Highlands@Survey")

#Send the mail
msg = "\nHello!" # The /n separates the message from the headers
server.sendmail("seddon-software@keme.co.uk", "seddon-software@keme.co.uk", msg)