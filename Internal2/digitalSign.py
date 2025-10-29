
#pip install cryptography(run this command in the terminal)
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Generate DSA private key
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# Message to sign
message = b'This is a confidential message.'

# Sign the message
signature = private_key.sign(message, hashes.SHA256())
print("Signature:", signature.hex())

# Verify the signature
try:
    public_key.verify(signature, message, hashes.SHA256())
    print("Signature is valid.")
except InvalidSignature:
    print("Signature is invalid.")
