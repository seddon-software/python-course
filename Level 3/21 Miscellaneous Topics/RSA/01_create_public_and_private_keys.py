from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives.asymmetric import rsa  
from cryptography.hazmat.primitives import serialization  
  
encryptedpass = "myverystrongpassword".encode()    # must be in bytes
  
def generate_RSA_keys():  
    private_key = rsa.generate_private_key(  
        public_exponent=65537,  
        key_size=2048,  
        backend=default_backend()  
    )  
    public_key = private_key.public_key()
    return public_key, private_key

def save_RSA_keys_in_PEM_format(name, public_key, private_key, password): 
    with open(f"keys/{name}_private_key.pem", "wb") as f:  
        f.write(private_key.private_bytes(  
            encoding=serialization.Encoding.PEM,  
            format=serialization.PrivateFormat.TraditionalOpenSSL,  
            encryption_algorithm=serialization.BestAvailableEncryption(password.encode()),  
            )  
        )  
    with open(f"keys/{name}_public_key.pem", "wb") as f:  
        f.write(public_key.public_bytes(  
            encoding=serialization.Encoding.PEM,  
            format=serialization.PublicFormat.SubjectPublicKeyInfo,  
        )  
    )

public_key, private_key = generate_RSA_keys()
save_RSA_keys_in_PEM_format("alice", public_key, private_key, 'alices_password')
public_key, private_key = generate_RSA_keys()
save_RSA_keys_in_PEM_format("bob", public_key, private_key, 'bobs_password')
