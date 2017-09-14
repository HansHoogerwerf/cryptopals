import codecs

__author__ = 'Hans'



def dehex(hexstring):
    return codecs.decode(hexstring,"hex")

def sameByteArray(array1, array2):
    if(len(array1) != len(array2)):
        return False
    else:
        for index in range(len(array1)):
            if(array1[index] != array2[index]):
                return False
        return True




def detectAESinECB(bytearray):
    partedbytearray = []
    part = 0
    for lenght in range(0, len(bytearray), 16):
        bit = bytearray[16 * part: 16 * (part + 1)]
        part +=1
        partedbytearray.append(bit)
        print(bit)
    for i in range(len(partedbytearray)):
        for j in range (i + 1, len(partedbytearray)):
            if(sameByteArray(partedbytearray[i],partedbytearray[j])):
                return True
    return False




filename = "C:/Users/Hans/Desktop/8.txt";
with open(filename) as f:
    content = f.readlines()
    print(content)
    encodeded = [x.strip() for x in content]
    for line in encodeded:
        dehexedline = dehex(line)
        if(detectAESinECB(dehexedline)):
            print("AESinECB = ", dehexedline)
            break
