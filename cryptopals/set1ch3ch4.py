__author__ = 'Hans'
encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
import binascii

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

#challange 3
def findString(encoded):
    nums = binascii.unhexlify(encoded)
    strings = []
    for key in range(256):
        string = '';
        for num in nums:
            string = string + (chr(num ^ key))

        strings.append(string)

    return max(strings, key=lambda s: findStringScore(s))

print(findString(encoded))


#challange 4
filename = "C:/Users/Hans/Desktop/4.txt";
with open(filename) as f:
    content = f.readlines()
    encodeded = [x.strip() for x in content]
    decoded = []
    for encoded in encodeded:
        try:
            decode = str(findString(encoded)).rstrip()
            decoded.append(findString(encoded))
        except UnicodeEncodeError as error:
            print("###################")
    print(max(decoded, key=lambda s: s.count(' ')))




