def caesar_encrypt(plaintext, shift):
    def shift_char(c):
        if c.isupper(): return chr((ord(c)-65+shift)%26+65)
        if c.islower(): return chr((ord(c)-97+shift)%26+97)
        return c
    return ''.join(shift_char(c) for c in plaintext)

def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# example
if __name__ == "__main__":
    print(caesar_encrypt("Hello, World!", 3))  # Khoor, Zruog!
    print(caesar_decrypt("Khoor, Zruog!", 3))  # Hello, World!
