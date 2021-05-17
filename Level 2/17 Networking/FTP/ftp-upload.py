def getPassword():
    homePages = '/Users/seddon/home/_Companies/CRS Enterprises/Technical/HomePages.txt'
    f = open(homePages, encoding="latin-1")
    password = f.readline().strip()
    f.close()
    return password

host     = "leopard.keme.net"
username = "seddon-software"
password = getPassword()
filename = "sample.html"
import ftplib
ftp_server = ftplib.FTP(host,port, username,password)
# Open the file you want to send
f = open(filename,"rb")
# Send it to the FTP server
resp = ftp_server.storbinary("STOR " + filename, f)
# Close the connection
ftp_server.close()



import webbrowser
url = "http://www.keme.co.uk/~seddon-software/" + filename
webbrowser.open_new_tab(url)
1







