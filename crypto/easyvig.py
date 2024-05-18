def encrypt(txt,key):
    encf = b""
    i = 0
    for c in txt:
        if i >= len(key):
            i = 0
        x = (c + key[i]) % 256 
        encf += x.to_bytes(1,'big')
        i+=1
    return encf

x = b'\x9e\xb5\xd4\xa8\x9c\xef\x98\x8c\x9d\xac\xb7\xabVz\xcf\xbe\xa1\x92\x7f\x86\xd7\x9aj\xac\xddY\x97\xad\x88\xa3mo\xb3\xb1\x88i\xae\xb4\xa6\x9bm\xb2\xae\x8aj\xb1\x85\xa8\x99\x9b\xb1\xddXh\x82\xb1\xd4\x9b\x9b\xaf\xab\x89h\x84\xb6\xa2\x9b\x98\xab\xdbYf\x82\x89\xaafm\xb2\xaaVf\xc8'
def decrypt(encf,key):
    txt = b""
    i = 0
    for c in encf:
        if i >= len(key):
            i = 0
        # decriptez fiecare caracter
        x = (c - key[i]) % 256
        txt += x.to_bytes(1,'big')
        i+=1
    return txt
# You know that the plaintext starts with:
# Secret flag
key = decrypt(x,b'Secret flag') # ii c
print(len(key))
for i in range(1,len(key)):
    try_key = key[:i]
    txt = decrypt(x,try_key)
    if b'CTF' in txt:
        print('The key is:',try_key)
        print('The flag is:',txt)
        break