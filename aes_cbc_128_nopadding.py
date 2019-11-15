import os
from base64 import b64decode
from hashlib import md5
from base64 import b64encode
from Crypto.Cipher import AES

class AES_ENCRYPT():
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        import base64
        cryptor = AES.new(self.key, self.mode, self.iv)
        length = 16
        count = len(text.encode('utf-8'))
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text1 = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text1)
        print(self.ciphertext.encode('hex'))
        #cryptedStr = str(base64.b64encode(self.ciphertext),encoding='utf-8')
        cryptedStr = str(base64.b64encode(self.ciphertext))
        return cryptedStr

        print('self.ciphertext:',self.ciphertext)
    def decrypt(self, text):
        import base64, json
        base_text = base64.b64decode(text)
        cryptor = AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(base_text)
        ne = plain_text.decode('utf-8').rstrip('\0')
        return ne

if __name__ == '__main__':
    aes_encrypt = AES_ENCRYPT('1234567890abcdef', '90abcdef12345678')
    text = '1234567890abcdefg'
    sign_data = aes_encrypt.encrypt(text)
    print(sign_data)
    data = aes_encrypt.decrypt(sign_data)
    print(data)
