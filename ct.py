def columnar_encrypt(plaintext, key):
    # key as list of integers representing column ranks (0-based or arbitrary but consistent)
    cols = len(key)
    rows = (len(plaintext) + cols - 1) // cols
    grid = [['X']*cols for _ in range(rows)]
    idx = 0
    for r in range(rows):
        for c in range(cols):
            if idx < len(plaintext):
                grid[r][c] = plaintext[idx]; idx += 1
            else:
                grid[r][c] = 'X'
    out = []
    for c in sorted(range(cols), key=lambda i: key[i]):
        for r in range(rows):
            out.append(grid[r][c])
    return ''.join(out)

def columnar_decrypt(ciphertext, key):
    cols = len(key)
    rows = (len(ciphertext) + cols - 1) // cols
    grid = [['']*cols for _ in range(rows)]
    idx = 0
    for c in sorted(range(cols), key=lambda i: key[i]):
        for r in range(rows):
            grid[r][c] = ciphertext[idx]; idx += 1
    return ''.join(grid[r][c] for r in range(rows) for c in range(cols)).rstrip('X')

# example
if __name__ == "__main__":
    key = [2,0,3,1]  # custom order mapping
    pt = "ATTACKATDAWN"
    ct = columnar_encrypt(pt, key)
    print(ct)
    print(columnar_decrypt(ct, key))
