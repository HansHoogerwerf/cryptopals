import base64
import codecs

__author__ = 'Hans'

hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

text = codecs.decode(hexstring,"hex")

print(base64.b64encode(bytes(text)))