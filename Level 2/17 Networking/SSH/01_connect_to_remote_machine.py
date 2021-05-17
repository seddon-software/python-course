import paramiko
import config

paramiko.util.log_to_file('ssh.log') # sets up logging
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def execute(cmd, hostname, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
        ssh.connect(hostname, port, username, password) 
        stdin, stdout, stderr = ssh.exec_command(cmd)
        print(stdout.readlines())
        ssh.close()
    except Exception as e:
        print('whoops: ' + str(e))

execute(cmd="uname -a", 
        hostname=config.HOSTNAME, port=22, 
        username=config.USER, password=config.PASSWORD)
