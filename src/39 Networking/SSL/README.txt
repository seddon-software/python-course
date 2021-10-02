This example shows how to use SSL between a client and a server on localhost.
To get this working on MacOS:

1. Check that OpenSSL is installed:
    openssl version -a

2. Create a private key and public key certificate using the script:
    create-certificates.py
    
   You can use all the defaults when running this program.  The private
   key and certificate will be created in the folder: certificates

3. On Mac and Linux, the server needs to use port 443.  However ports below
   1024 can only be accessed by root, so you need to use port forwarding.
   This is handled differently on Mac and Linux.  There is no restriction 
   on port use in Windows. 

   On MacOS: 
       echo "
        rdr pass inet proto tcp from any to any port 443 -> 127.0.0.1 port 8443
        " | sudo pfctl -ef -
   On Linux (not tested):
       iptables -t nat -A OUTPUT -p tcp --dport 443 -d 127.0.0.1 -j DNAT --to-destination 127.0.0.1:8443
   
4. Fire up the server
    python ssl-server.py

5. Fire up the client:
    python ssl-client.py
    Assuming SSL is setup:

Free Certificates:
    startssl
    letsencrypt

Implementation of the TLS/SSL protocols
    S2N:  https://github.com/awslabs/s2n
