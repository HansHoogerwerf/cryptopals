from base64 import b64decode
import codecs
from Crypto.Cipher import AES

obj = AES.new(codecs.encode("YELLOW SUBMARINE"), AES.MODE_ECB)

text = b64decode("".join(list(open("C:/Users/Hans/Desktop/7.txt", "r"))))

plain = obj.decrypt(text)

print(plain)
