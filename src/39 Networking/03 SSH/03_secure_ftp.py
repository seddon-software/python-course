import paramiko
import config   # contains HOSTNAME, USER and PASSWORD


class Server(object):
    def __init__(self, username, password, hostname, port=22):
        self.transport = paramiko.Transport((hostname, port))
        self.transport.connect(username=username, password=password)
        self.sftp = paramiko.SFTPClient.from_transport(self.transport)

    def upload(self, local, remote):
        self.sftp.put(local, remote)

    def download(self, remote, local):
        self.sftp.get(remote, local)

    def close(self):
        if self.transport.is_active():
            self.sftp.close()
            self.transport.close()

    # with-statement support
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.close()


paramiko.util.log_to_file('ssh.log') # sets up logging

ubuntuServer = Server(username=config.USER,
                      password=config.PASSWORD, 
                      hostname=config.HOSTNAME, 
                      port=22) 

# upload and download a file
import os
os.remove("files/test2.copy.txt") 
ubuntuServer.upload(local="files/test2.txt", remote="test2.txt")
ubuntuServer.download(remote="test2.txt", local="files/test2.copy.txt")
os.system("ls -l files")
ubuntuServer.close()

