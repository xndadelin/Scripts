from pwn import *
"""
Welcome, traveler. Let's play a few games. Here's the only command I will accept:
Move the top disk of tower {x} to tower {y}
({x} and {y} are numbers from 1 to 3)
Let's begin!
"""
"""
Current tower state:
Tower #1: 3 2 1
Tower #2: 
Tower #3: 
Put everything on the last tower (#3)
"""
r = remote('35.198.79.69', '32088')
prompt = r.recv()
""" # send the commands
r.sendline('Move the top disk of tower 1 to tower 3')
r.sendline('Move the top disk of tower 1 to tower 2')
r.sendline('Move the top disk of tower 3 to tower 2')
r.sendline('Move the top disk of tower 1 to tower 3')
r.sendline('Move the top disk of tower 2 to tower 1')
r.sendline('Move the top disk of tower 2 to tower 3')
r.sendline('Move the top disk of tower 1 to tower 3')
# get the flag
r.recv()
Current tower state:
Tower #1: 3
Tower #2: 2
Tower #3: 1
Put everything on the last tower (#3)
r.sendline('Move the top disk of tower 1 to tower 3')
r.sendline('Move the top disk of tower 1 to tower 2')
r.sendline('Move the top disk of tower 3 to tower 2')
r.sendline('Move the top disk of tower 1 to tower 3')
r.sendline('Move the top disk of tower 2 to tower 1')
r.sendline('Move the top disk of tower 2 to tower 3')
r.sendline('Move the top disk of tower 1 to tower 3')
r.recv()
Current tower state:
Tower #1: 3 2
Tower #2: 
Tower #3: 1
Put everything on the last tower (#3)
r.sendline('Move the top disk of tower 1 to tower 3')
r.sendline('Move the top disk of tower 1 to tower 2')
r.sendline('Move the top disk of tower 3 to tower 2')
r.sendline('Move the top disk of tower 1 to tower 3')
r.sendline('Move the top disk of tower 2 to tower 1')
r.sendline('Move the top disk of tower 2 to tower 3')
r.sendline('Move the top disk of tower 1 to tower 3')
print(r.interactive()) """
""" for i in range(100):
    r.sendline('Move the top disk of tower 1 to tower 3')
    r.sendline('Move the top disk of tower 1 to tower 2')
    r.sendline('Move the top disk of tower 3 to tower 2')
    r.sendline('Move the top disk of tower 1 to tower 3')
    r.sendline('Move the top disk of tower 2 to tower 1')
    r.sendline('Move the top disk of tower 2 to tower 3')
    r.sendline('Move the top disk of tower 1 to tower 3')
    print(r.recv()) """
# im giving up