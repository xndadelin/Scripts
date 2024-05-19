# heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2
"""
Our data got corrupted on the way here. 
Luckily, nothing got replaced, but every block of 3 got scrambled around! 
The first word seems to be three letters long, maybe you can use that to recover the rest of the message.
"""
# The first words are "The flag is"
# so basically, based on the hint that every block of 3 got scrambled around, we will unscramble the text by grouping the text into blocks of 3 and then unscramble them
# heT -> The, so block[0] = block[2], block[1] = block[1], block[2] = block[0]
flag = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"
for i in range(0, len(flag), 3):
    block = flag[i:i+3]
    print(block[2] + block[0] + block[1], end="")