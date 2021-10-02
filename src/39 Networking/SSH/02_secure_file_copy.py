import paramiko
import config
from paramiko.ssh_exception import SSHException

paramiko.util.log_to_file('ssh.log') # sets up logging

def secureFileCopy(localFile, remoteFile, hostname, port, username, password):
    try:
        transport = paramiko.Transport((hostname, port))
        transport.connect(username = username, password = password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(remotepath=remoteFile, localpath=localFile)
    except SSHException as e:
        print(e)
    except IOError as e:
        print(e.errno, e.strerror)
    except Exception as e:
        print(e.errno, e.strerror)
    finally:
        try:
            sftp.close()
            transport.close()
        except:
            pass
    

secureFileCopy(localFile="files/test1.txt", 
               remoteFile="test1.txt", 
               hostname=config.HOSTNAME, 
               port=22, 
               username=config.USER, 
               password=config.PASSWORD)


