############################################################
#
#    main.py
#
############################################################

import smtplib
server = smtplib.SMTP('mail.btinternet.com')

USER = "seddon_software@btinternet.com"

server.login(user=USER, password=PASSWORD)
try:
    server.sendmail(USER, USER, \
    """To: seddon-software@btinternet.com
    From: seddon-software@keme.co.uk
    Beware the Ides of March.
    """) 
except Exception as e:
    print(e)
server.quit()



