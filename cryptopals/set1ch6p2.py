import codecs

import base64

string1 = "this is a test"
string2 = "wokka wokka!!!"

scores =[
    ["e", 0.12],
    ["t", 0.09],
    ["a", 0.08],
    ["o", 0.07],
    ["i", 0.069],
    ["n", 0.067],
    [" ", 0.15]
]

def xor(b1, b2):
    b = bytearray(len(b1))
    for i in range(len(b1)):
        b[i] = b1[i] ^ b2[i]
    return b

def hamming_distance(enc_str1, enc_str2):
    differing_bits = 0
    for byte in xor(enc_str1, enc_str2):
        differing_bits += bin(byte).count("1")
    return differing_bits

#from stackoverflow
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def hammingDistance(string1, string2):
    distance = 0
    binString1 = tobits(string1)
    binString2 = tobits(string2)
    for (i ,bit) in enumerate(binString1):
        if binString1[i] != binString2[i]:
            distance +=1
    return distance

b1 = codecs.encode("this is a test")
b2 = codecs.encode("wokka wokka!!!")

distance = hamming_distance(b1, b2)
distance2 = hammingDistance(string1, string2)

print(distance)
print(distance2)


b = base64.b64decode("".join(list(open("C:/Users/Hans/Desktop/6.txt", "r"))))
decoded = codecs.decode(b, 'utf-8')


first5 = decoded[:5]
second5 = decoded[:10][-5:]

print(first5)
print(second5)

decodedhd = hammingDistance(first5, second5)

print(decodedhd)

def findKeysize(encryptedtext):
    keysizes = []
    for size in range(2,41):
        firstpart = encryptedtext[:size]
        secondpart = encryptedtext[:size * 2][-size:]
        thirdpart = encryptedtext[:size * 3][-size:]
        fourthpart = encryptedtext[:size * 4][-size:]
        output = hammingDistance(firstpart, secondpart)
        output += hammingDistance(firstpart, thirdpart)
        output += hammingDistance(firstpart, fourthpart)
        output += hammingDistance(secondpart, thirdpart)
        output += hammingDistance(secondpart, fourthpart)
        output += hammingDistance(thirdpart, fourthpart)

        keysizes.append([size, output / (size * 6)])
    return keysizes

sizes = findKeysize(decoded)

minsize = min(sizes , key=lambda s: s[1])[0]

minsizes = sorted(sizes , key=lambda s: s[1])[:4]

best_keysize = minsizes[0]

print(best_keysize)

def transposeBlocks(block, keysize):

    blocks = []

    for i in range(keysize):
        blocks.append('')

    for index in range(len(block)):
        blocks[index%keysize] += block[index]



    return blocks

blocks = transposeBlocks(decoded, best_keysize[0])


def findStringScore(string):
    score = 0
    string = string.lower()
    for char in string:
        for scorevalue in scores:
            if char == scorevalue[0]:
                score += scorevalue[1]
                break;
    return score

def findString(encoded):
    strings = []
    for key in range(256):
        string = '';
        for char in encoded:
            string = string + (chr(ord(char) ^ key))

        strings.append([key, string])

    return max(strings, key=lambda s: findStringScore(s[1]))


decryptedBlocks = []

print("block len", len(blocks[0]))

key = ""

for singleCypherBlock in blocks:
    decrypted_block_and_key = findString(singleCypherBlock)
    decrypted_block = decrypted_block_and_key[1]
    key += chr(decrypted_block_and_key[0])
    decryptedBlocks.append(decrypted_block)

print("key:", key)
plainTextInArrays = []
for i in range(len(decryptedBlocks[0])):
    plainTextInArrays.append("")

for index in range(len(decryptedBlocks)):
    for j in  range(len(decryptedBlocks[index])):
        plainTextInArrays[j] += decryptedBlocks[index][j]

print(plainTextInArrays)

plaintext = ""
for string3 in plainTextInArrays:
    plaintext += string3
print(plaintext)