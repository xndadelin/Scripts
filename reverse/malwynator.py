# FWI~\3xbDu&b$Qi6Fw&g€
# this is caesar cipher shifted by 3, so we will shift it back by 3
string = "FWI~\3xbDu&b$Qi6Fw&g€"
flag = ""
for i in range(0, len(string)):
    flag += chr(ord(string[i]) - 3)

print("".join(flag))