import itertools
import base64

def string_xor(s, key):
    key = key * (len(s) // len(key) + 1)
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(s, key)) 

enc64 = "dHNkdktTAVUHAABUA1VWVgIHBAlSBAFTBAMFUwECAgcAAAFWAFUFCFMACFFUAwQAVgBSBwQJBVZTAFYGCQYHVQABB1IJTQ=="
key = 0x30
# encode enc64 to hex
enchex = base64.b64decode(enc64).hex()
# every 2 characters is a byte, xor with key
dec = ''.join([chr(int(enchex[i:i+2], 16) ^ key) for i in range(0, len(enchex), 2)])
print(dec)