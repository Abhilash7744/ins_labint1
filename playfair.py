def _playfair_matrix(key):
    s = "".join(dict.fromkeys(key.upper().replace("J","I")))
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for c in alphabet:
        if c not in s: s += c
    return [list(s[i*5:(i+1)*5]) for i in range(5)]

def _prep_text_playfair(text):
    t = text.upper().replace("J","I")
    t = ''.join(ch for ch in t if ch.isalpha())
    res = []
    i = 0
    while i < len(t):
        a = t[i]
        b = t[i+1] if i+1 < len(t) else 'X'
        if a == b:
            res.append(a + 'X')
            i += 1
        else:
            res.append(a + b)
            i += 2
    if len(res[-1]) == 1: res[-1] += 'X'
    return res

def _find_pos(matrix, ch):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch: return i, j

def playfair_encrypt(plaintext, key):
    m = _playfair_matrix(key)
    pairs = _prep_text_playfair(plaintext)
    out = []
    for a,b in pairs:
        x1,y1 = _find_pos(m,a)
        x2,y2 = _find_pos(m,b)
        if x1 == x2:
            out.append(m[x1][(y1+1)%5] + m[x2][(y2+1)%5])
        elif y1 == y2:
            out.append(m[(x1+1)%5][y1] + m[(x2+1)%5][y2])
        else:
            out.append(m[x1][y2] + m[x2][y1])
    return ''.join(out)

def playfair_decrypt(ciphertext, key):
    m = _playfair_matrix(key)
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    out = []
    for a,b in pairs:
        x1,y1 = _find_pos(m,a)
        x2,y2 = _find_pos(m,b)
        if x1 == x2:
            out.append(m[x1][(y1-1)%5] + m[x2][(y2-1)%5])
        elif y1 == y2:
            out.append(m[(x1-1)%5][y1] + m[(x2-1)%5][y2])
        else:
            out.append(m[x1][y2] + m[x2][y1])
    return ''.join(out)

# example
if __name__ == "__main__":
    ct = playfair_encrypt("Hide the gold", "keyword")
    print(ct)
    print(playfair_decrypt(ct, "keyword"))
