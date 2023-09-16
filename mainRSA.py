from fractions import Fraction

def EncryptedText(TextForChipheer, OpenExponenta, n):
    TextForChipheer = [ord(c) for c in TextForChipheer]
    len_TextForChipheer = len(TextForChipheer)
    encrypted_blocks = [0] * len_TextForChipheer
    i = 0 
    while i != len_TextForChipheer:
        encrypted_blocks[i] = power_mod(TextForChipheer[i], OpenExponenta, n)
        i = i + 1
    return (encrypted_blocks)

def DecryptedText(encrypted_blocks, d, n):
    len_encrypted_blocks = len(encrypted_blocks)
    decrypted_blocks = [0] * len_encrypted_blocks
    i = 0
    while i != len_encrypted_blocks:
        decrypted_blocks[i] = power_mod(encrypted_blocks[i], d, n)
        i = i + 1
    text = ""
    for block in decrypted_blocks:
        text += chr(block)
    return (text)

def power_mod(x, y, z):
    result = pow(x, y, z)
    return result

def FuctionEilera(p, q):
    Fi = (p - 1) * (q - 1)
    return Fi 

def main():
    p = 53
    q = 67
    e = 1531
    text_for_chipfer = "Hello World!"
    print("text_for_chipfer = " + str(text_for_chipfer))
    n = p * q
    print ("n = " + str(n))
    Fuction_Eilera = FuctionEilera(p, q)
    print("Fuction_Eilera = " + str(Fuction_Eilera))
    open_key = [e, n]
    print("open_key = " + str(open_key))
    lock_key = [power_mod(e, -1, Fuction_Eilera), n]
    print("lock_key = " + str(lock_key))
    block = EncryptedText(text_for_chipfer, open_key[0], open_key[1])
    block_str = ''.join(str(c) for c in block)
    print("EncryptedText = " + str(block_str))
    print("DecryptedText = " + str(DecryptedText(block, lock_key[0], lock_key[1])))

if __name__ == '__main__':
    main()
