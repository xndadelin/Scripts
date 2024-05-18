secret_message =  [805, 822, 808, 816, 817, 822, 821, 807, 805, 823, 820, 807, 807, 816, 817, 809, 810, 804, 823, 822, 803, 808, 823, 816, 816, 827, 825, 803, 827, 822, 817, 810, 811, 806, 807, 803, 815, 807, 821, 821, 803, 809, 807]
# we can see that the message is a list of numbers
# we can try to convert them to characters, but the numbers are too high to be ascii values, so we can assume that we have to find an offset to decrypt the message
# we can try to find the offset by brute force

def decrypt(message, offset):
    return ''.join([chr(x - offset) for x in message])

for i in range(1, 800):
    print(decrypt(secret_message, i))

# CTFNOTSECUREENOGHBUTAFUNNYWAYTOHIDEAMESSAGE, the offset is 800