import ftplib

HOST     = "192.168.1.110"
USER     = "user1"
PASSWORD = "user1"
filename = "sample.html"
try:
    ftp_server = ftplib.FTP(host=HOST, user=USER, passwd=PASSWORD)
    print(ftp_server)
    # Open the file you want to send
    f = open(filename,"rb")
    # Send it to the FTP server
    resp = ftp_server.storbinary(f"STOR  {filename}", f)
except Exception as e:
    print(e)

# Close the connection
ftp_server.close()




