from random import randint
from pwn import *
from Crypto.Util.number import inverse
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key
r = remote('35.198.79.69', 30604)
r.recvuntil("x? ")

# Given parameters
q = 65537
g = 31337

# Input the provided value of x
x = 2
r.sendline(str(x))

print(r.recvuntil("value of h: "))
# Calculate h = g^x mod q
h = pow(g, x, q)
r.sendline(str(h))

print(r.recvuntil("int): "))
# Message to sign
m = int.from_bytes(b'hi', 'big')
print(m)
r.sendline(str(m))

print(r.recvuntil("use? "))
# Choose a value for y
y = pow(g, x, q)
r.sendline(str(y))
enc_mes = []
k = gen_key(q)
s = pow(h, k, q)
p = pow(g, k, q)
for i in range(0, len(m)):
    enc_mes[i] = s * ord(enc_mes[i])

print(enc_mes)