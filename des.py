# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def des_encrypt_cbc(plaintext_bytes, key8):
    iv = get_random_bytes(8)
    cipher = DES.new(key8, DES.MODE_CBC, iv)
    ct = cipher.encrypt(pad(plaintext_bytes, 8))
    return iv + ct  # prepend IV

def des_decrypt_cbc(iv_ct, key8):
    iv = iv_ct[:8]
    ct = iv_ct[8:]
    cipher = DES.new(key8, DES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), 8)

# example
if __name__ == "__main__":
    key = b'8bytekey'  # must be 8 bytes
    pt = b"Secret message for DES"
    ct = des_encrypt_cbc(pt, key)
    print("cipher (hex):", ct.hex())
    print("decrypted:", des_decrypt_cbc(ct, key))
