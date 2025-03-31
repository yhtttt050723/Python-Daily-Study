from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_cast(encrypted_file):
    with open(encrypted_file, 'rb') as f:
        ciphertext = f.read()
    key = b'__ELPSYCONGROO__'
    iv = b'114_514_1919_810'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode('utf-8')

decrypted_data = decrypt_cast(r"D:\CTFshow misc\record.cast" )
print(decrypted_data[:10000])
