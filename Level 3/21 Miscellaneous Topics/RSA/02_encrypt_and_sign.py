from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives.asymmetric import padding  
from cryptography.hazmat.primitives import hashes  
from cryptography.hazmat.primitives.serialization import load_pem_private_key  
from cryptography.hazmat.primitives.serialization import load_pem_public_key  
from cryptography.hazmat.primitives import serialization
  
  
# 1. Alice encrypts her message with the Bob’s public key
# 2. Alice signs her message with her private key
##     5. Maria has everything she needs to send her secret message to me now:
##     6. When I receive Maria’s message the first thing I have to do to decrypt the message is:
##     7. Last resort, I should check the message origin to determine the identity of message emisor:


plaintextMessage = "This is a message from alice.".encode()  
bobPubKey = load_pem_public_key(open('keys/bob_public_key.pem', 'rb').read(),default_backend())  
ciphertext = bobPubKey.encrypt(  
    plaintextMessage,  
    padding.OAEP(  
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  
            algorithm=hashes.SHA256(),  
            label=None  
  )  
)  

encryptedpass = "alices_password".encode()
alicePrivKey = load_pem_private_key(open('keys/alice_private_key.pem', 'rb').read(),encryptedpass,default_backend())  
signed_message = alicePrivKey.sign(
    ciphertext,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# write encrypted message to file
f = open('out/encrypted_message', 'wb')
f.write(ciphertext)
f.close()
# write signed message to file
f = open('out/signed_message', 'wb')
f.write(signed_message)
f.close()

  
# deccryptedMessage = alicePrivKey.decrypt(  
#     ciphertext,  
#     padding.OAEP(  
#             mgf=padding.MGF1(algorithm=hashes.SHA256()),  
#             algorithm=hashes.SHA256(),  
#             label=None  
#   )  
# )  
# print(deccryptedMessage.decode(encoding="utf-8"))

