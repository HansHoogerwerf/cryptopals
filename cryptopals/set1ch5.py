__author__ = 'Hans'
import binascii

message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

def repeatingKeyXor(key, string):
    output = ''
    for (i ,char) in enumerate(string):
        index = i % len(key)
        xorchar = key[index]
        tempChar = chr(ord(char) ^ ord(xorchar))

        output += tempChar
    return binascii.hexlify(str.encode(output))

print(repeatingKeyXor("ICE", message))



