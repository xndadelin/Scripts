# 89 50 4e 47 are the first four bytes of a PNG file
# this is mine: 89 47 50 4e
# so I need to change the endianness of the bytes
# so wee need to change the order of the bytes
correct = [0x89, 0x50, 0x4e, 0x47]
with open('/home/xndadelin/Desktop/python_scripts/steg/custom.png', 'rb') as picture:
    png = picture.read()
    png = bytearray(png)
    # padding the image with 0s to make it divisible by 4
    while len(png) % 4 != 0:
        png.append(0)
    # prelucrez fiecare 4 biti la rand
    custom = []
    for i in range(0, len(png), 4):
        custom.append(png[i])
        custom.append(png[i+2])
        custom.append(png[i+3])
        custom.append(png[i+1])
    with open('/home/xndadelin/Desktop/python_scripts/steg/custom-endianness.png', 'wb') as new_picture:
        new_picture.write(bytearray(custom))
        print('Endianness changed')