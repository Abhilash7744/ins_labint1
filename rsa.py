from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_generate(bits=2048):
    key = RSA.generate(bits)
    private_pem = key.export_key()
    public_pem = key.publickey().export_key()
    return private_pem, public_pem

def rsa_encrypt(message_bytes, public_pem):
    pub = RSA.import_key(public_pem)
    cipher = PKCS1_OAEP.new(pub)
    return cipher.encrypt(message_bytes)

def rsa_decrypt(cipher_bytes, private_pem):
    priv = RSA.import_key(private_pem)
    cipher = PKCS1_OAEP.new(priv)
    return cipher.decrypt(cipher_bytes)

# example
if __name__ == "__main__":
    priv, pub = rsa_generate(2048)
    pt = b"RSA message"
    ct = rsa_encrypt(pt, pub)
    print("cipher (hex):", ct.hex()[:100]+"...")
    print("decrypted:", rsa_decrypt(ct, priv))
