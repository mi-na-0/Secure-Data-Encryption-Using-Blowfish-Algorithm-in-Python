from Crypto.Cipher import Blowfish
from Crypto import Random

def encrypt(plaintext, key):
    bs = Blowfish.block_size
    iv = Random.new().read(bs)
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = pad(plaintext)
    ciphertext = iv + cipher.encrypt(plaintext.encode())
    return ciphertext

def decrypt(ciphertext, key):
    bs = Blowfish.block_size
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]
    cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext)).decode('utf-8')
    return plaintext

def pad(s):
    return s + (Blowfish.block_size - len(s) % Blowfish.block_size) * chr(Blowfish.block_size - len(s) % Blowfish.block_size)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

# Example usage:
if __name__ == '__main__':
    key = b'SecretKey'  # Replace with your key
    plaintext = 'This is a test message'
    
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)
    
    print(f'Plaintext: {plaintext}')
    print(f'Ciphertext: {ciphertext}')
    print(f'Decrypted Text: {decrypted_text}')
