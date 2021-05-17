import os

os.chdir("certificates")
os.system("openssl genrsa -des3 -passout pass:x -out server.pass.key 2048")
os.system("openssl rsa -passin pass:x -in server.pass.key -out server.key")
os.system("rm server.pass.key")
os.system("openssl req -new -key server.key -out server.csr")
os.system("openssl x509 -req -sha256 -days 365 -in server.csr -signkey server.key -out server.crt")
