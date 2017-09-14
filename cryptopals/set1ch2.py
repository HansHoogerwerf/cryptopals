__author__ = 'Hans'
import codecs


input = "1c0111001f010100061a024b53535009181c"
xor = "686974207468652062756c6c277320657965"

byteInput = int(input, 16)
byteXor = int(xor, 16)

print(hex(byteInput ^ byteXor)[2:])
