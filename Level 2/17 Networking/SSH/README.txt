1) make sure sshd is running on ubuntu machine
    ps -ef | grep sshd
2) check the IP of the ubuntu host
    ifconfig
3) check SSH is on port 22
    netstat -an | grep :22
4) check for demo account (tom):
    compgen -u
5) password is same as user name:
    tom
6) VirtualBox needs to be setup to use Bridged Adapter
   check with ping from host
    ping 192.168.0.68
    
    