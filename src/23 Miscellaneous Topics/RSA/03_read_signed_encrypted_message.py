from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key  
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature


# read encrypted and signed messages
f = open('out/encrypted_message', 'rb')
ciphertext = f.read()
f.close()

f = open('out/signed_message', 'rb')
signed_message = f.read()
f.close()

# load keys
encryptedpass = "bobs_password".encode()
bobPubKey = load_pem_public_key(open('keys/bob_public_key.pem', 'rb').read(),default_backend())  
bobPrivKey = load_pem_private_key(open('keys/bob_private_key.pem', 'rb').read(),encryptedpass,default_backend())  

# 1. Bob decrypts with his private key 
decryptedMessage = bobPrivKey.decrypt(  
    ciphertext,  
    padding.OAEP(  
            mgf=padding.MGF1(algorithm=hashes.SHA256()),  
            algorithm=hashes.SHA256(),
            label=None  
  )  
)  

# 2. Bob verifies messages with Alice's public key
alicePubKey = load_pem_public_key(open('keys/alice_public_key.pem', 'rb').read(),default_backend())  
try:    
    alicePubKey.verify(
        signed_message,
        #decryptedMessage,
        ciphertext,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
except InvalidSignature as e:
    print(f"error: {e}")
except:
    print("Unknown error")
else:
    print("Verified message is from Alice")
    print(f"Message: {decryptedMessage.decode()}")
