# Hill Cipher Implementation (Encryption + Decryption)

def mod_inverse(a, m):
    # Extended Euclidean Algorithm to find modular inverse
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inv(matrix, modulus):
    # Only works for 2x2 matrix
    det = int(matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0])
    det = det % modulus
    det_inv = mod_inverse(det, modulus)
    if det_inv is None:
        raise Exception("Matrix is not invertible under modulo", modulus)

    inv_matrix = [[matrix[1][1]*det_inv % modulus, -matrix[0][1]*det_inv % modulus],
                  [-matrix[1][0]*det_inv % modulus, matrix[0][0]*det_inv % modulus]]
    
    # Ensure all entries are positive
    for i in range(2):
        for j in range(2):
            inv_matrix[i][j] = inv_matrix[i][j] % modulus

    return inv_matrix

def encrypt(message, key_matrix):
    message = message.replace(" ", "").lower()
    if len(message) % 2 != 0:
        message += 'x'   # padding

    result = ""
    for i in range(0, len(message), 2):
        pair = [ord(message[i]) - 97, ord(message[i+1]) - 97]
        c1 = (key_matrix[0][0]*pair[0] + key_matrix[0][1]*pair[1]) % 26
        c2 = (key_matrix[1][0]*pair[0] + key_matrix[1][1]*pair[1]) % 26
        result += chr(c1 + 97) + chr(c2 + 97)
    return result

def decrypt(cipher, key_matrix):
    inv_matrix = matrix_mod_inv(key_matrix, 26)
    result = ""
    for i in range(0, len(cipher), 2):
        pair = [ord(cipher[i]) - 97, ord(cipher[i+1]) - 97]
        p1 = (inv_matrix[0][0]*pair[0] + inv_matrix[0][1]*pair[1]) % 26
        p2 = (inv_matrix[1][0]*pair[0] + inv_matrix[1][1]*pair[1]) % 26
        result += chr(p1 + 97) + chr(p2 + 97)
    return result

# Example usage:
key = [[3, 3],
       [2, 5]]  # Key matrix (must be invertible mod 26)

msg = "hillcipher"
enc = encrypt(msg, key)
dec = decrypt(enc, key)

print("Original Message:", msg)
print("Encrypted Message:", enc)
print("Decrypted Message:", dec)
