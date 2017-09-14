import base64
import binascii

__author__ = 'Hans'

string1 = "this is a test"
string2 = "wokka wokka!!!"

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

scores =[
    ["e", 0.12],
    ["t", 0.09],
    ["a", 0.08],
    ["o", 0.07],
    ["i", 0.069],
    ["n", 0.067],
    [" ", 0.15]
]

def findStringScore(string):
    score = 0
    string = string.lower()
    for char in string:
        for scorevalue in scores:
            if char == scorevalue[0]:
                score += scorevalue[1]
                break;
    return score

def break_single_key_xor(b1):
    max_score = -1
    english_plaintext = None
    key = None

    for i in range(256):
        b2 = [i] * len(b1)
        plaintext = bytes(xor(b1, b2))
        pscore = findStringScore(plaintext)

        if pscore > max_score or not max_score:
            max_score = pscore
            english_plaintext = plaintext
            key = chr(i)
    return key, english_plaintext


scores =[
    ["e", 0.12],
    ["t", 0.09],
    ["a", 0.08],
    ["o", 0.07],
    ["i", 0.069],
    ["n", 0.067],
    [" ", 0.15]
]

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
    decodedHEx = binascii.unhexlify(encoded.rstrip())
    strings = []
    for key in range(256):
        string = '';
        for char in decodedHEx:
            string = string + (chr(char ^ key))

        strings.append(string)

    return max(strings, key=lambda s: findStringScore(s))


#from stackoverflow
def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

#from ch5
def repeatingKeyXor(key, string):
    output = ''
    for (i ,char) in enumerate(string):
        index = i % len(key)
        xorchar = key[index]
        tempChar = chr(ord(char) ^ ord(xorchar))
        output += tempChar
    return binascii.hexlify(str.encode(output))

def hammingDistance(string1, string2):
    distance = 0
    binString1 = tobits(string1)
    binString2 = tobits(string2)
    for (i ,bit) in enumerate(binString1):
        if binString1[i] != binString2[i]:
            distance +=1

    return distance

def findNormilizedEditDistance(keysize, block):
    firstblock = block[:keysize]
    secondblock = block[:keysize * 2][-keysize:]
    return (hamming_distance(firstblock, secondblock) / keysize)

def transposeBlocks(block, keysize):

    print("start blocking")
    print(block)
    block_bytes = [[] for _ in range(keysize)]
    for i, byte in enumerate(block):
        block_bytes[i % keysize].append(byte)

    keys = ""
    for bbytes in block_bytes:
        keys += break_single_key_xor(bbytes)[0]

    key = bytearray(keys.encode() * len(block))
    plaintext = bytes(xor(block, key))

    print (keys)
    print (keysize)
    print (plaintext)
    return block_bytes

# def transposeBlocks(blocks, keysize):
#     transposedblocks = []
#     for key in range(keysize):
#         transposedblocks.append()
#     for block in blocks:
#         for index in range(len(block)):
#             transposedblocks[index] += block[index]
#     return transposedblocks

def main(filename):
    with open(filename) as f:

        normilizedEditDistances = []

        block = ""
        content = f.readlines()
        encodeded = [x.strip() for x in content]
        for encoded in encodeded:
            block += encoded

        #debase64 the information
        block = base64.b64decode(block)



        # print(block)

        for keysize in range(2, 41):
            editsize = findNormilizedEditDistance(keysize, block)
            normilizedEditDistances.append([keysize, editsize])
        smallest = min(normilizedEditDistances, key=lambda s: s[1])
        print(smallest)
        #
        transposedblocks = transposeBlocks(block, smallest[0])



        # transposedblocks = transposeBlocks(blocks, smallest[0])








main("C:/Users/Hans/Desktop/6.txt")





# print(hammingDistance(string1, string2))


#internet one



def findKeyLenght():
    b = bytearray("".join(list(open("6.txt", "r"))).decode("base64"))
    normalized_distances = []
    for KEYSIZE in range(2, 40):
        b1 = b[: KEYSIZE]
        b2 = b[KEYSIZE: KEYSIZE * 2]
        b3 = b[KEYSIZE * 2: KEYSIZE * 3]
        b4 = b[KEYSIZE * 3: KEYSIZE * 4]

        normalized_distance = float(
            hamming_distance(b1, b2) +
            hamming_distance(b2, b3) +
            hamming_distance(b3, b4)
        ) / (KEYSIZE * 3)

        normalized_distances.append(
            (KEYSIZE, normalized_distance)
        )
    print(normalized_distances)