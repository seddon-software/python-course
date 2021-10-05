############################################################
#
#    main.py
#
############################################################

import smtplib
server = smtplib.SMTP('smtp.gmail.com')

server.sendmail('assess.my.deal.2018', 'My-team-is-spurs.', \
"""To: abc-software@abc.com
From: seddon-software@keme.co.uk
Beware the Ides of March.
""") 

server.quit()



