from pwn import *
import threading

context.log_level = 'critical'
pin = 0
def run_math(start, end):
    for number in range(start, end):
        p = process('/home/xndadelin/Desktop/Scripts/reverse/math.out')
        p.recvuntil('here:\n')
        p.sendline(str(number))
        output = p.recvall()
        if output != b'':
            pin = number
            print(f"Pin: {number}, Output: {output}")
            p.close()
            return
        p.close()

# Multithreading
# Each thread is responsible for a range of 1000 numbers
threads = []
num_threads = 10 

for i in range(num_threads):
    start = i * 1000
    end = start + 1000
    t = threading.Thread(target=run_math, args=(start, end))
    threads.append(t)
    t.start()

# Join all threads
for t in threads:
    t.join()

print(f"Pin: {pin}")