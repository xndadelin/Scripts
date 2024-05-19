# rsa algoritm
import math
from Crypto.Util.number import long_to_bytes
# def gcd(a, b):
#    if b == 0:
#       return a
#    else:
#       return gdc(b, a % b) 

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(e, phi):
    gcd, x, y = gcd_extended(e, phi)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % phi

sieve = [1] * 1000000
sieve[0] = sieve[1] = 0
sieve[2] = 1
primes = []

def sieve_of_eratosthenes(n):
    for i in range(3, int(math.sqrt(n) + 1)):
        if sieve[i] == 1:
            for j in range(i * i, n, i):
                sieve[j] = 0
    for i in range(2, n):
        if sieve[i] == 1:
            primes.append(i)

def is_prime(a):
    if a < 2:
        return False
    else:
        d = 0
        while primes[d] * primes[d] <= a:
            if a % primes[d] == 0:
                return False
            d += 1
        return True
def encrypt(e, n):
    message = input("Enter the message: ")
    enc_mes = []

    for char in message:
        enc_mes.append(ord(char))

    enc_mes = [pow(char, e, n) for char in enc_mes]
    return enc_mes

def decrypt(d, n, enc_mes):
    dec_mes = [chr(pow(char, d, n)) for char in enc_mes]
    return "".join(dec_mes)

# sieve_of_eratosthenes(1000000000)

""" p = int(input("Enter the value of p: "))
if not is_prime(p):
    raise ValueError("p is not prime")

q = int(input("Enter the value of q: "))
if not is_prime(q):
    raise ValueError("q is not prime")
 """
""" n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = modular_inverse(e, phi) """

""" if __name__ == "__main__":
    print("=============================================")
    print("Welcome to RSA encryption and decryption")
    print("1. Encrypt")
    print("2. Decrypt")
    print("=============================================")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enc_mes = encrypt(e, n)
        print("Encrypted message: ", enc_mes)
    elif choice == 2:
        enc_mes = list(map(int, input("Enter the encrypted message: ").split()))
        dec_mes = decrypt(d, n, enc_mes)
        print("Decrypted message: ", dec_mes)
    else:
        print("Invalid choice") """

"""
Decrypt my super sick RSA:
c: 8533139361076999596208540806559574687666062896040360148742851107661304651861689
n: 769457290801263793712740792519696786147248001937382943813345728685422050738403253
e: 65537
Hint: Bits are expensive, I used only a little bit over 100 to save money
"""
# found using factordb
p = 1617549722683965197900599011412144490161 
q = 475693130177488446807040098678772442581573
n = p * q
phi = (p - 1) * (q - 1)
e = 65537
d = modular_inverse(e, phi)
c = 8533139361076999596208540806559574687666062896040360148742851107661304651861689
decrypted = pow(c, d, n)
print(long_to_bytes(decrypted))