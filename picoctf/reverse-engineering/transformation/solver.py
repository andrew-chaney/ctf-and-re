enc = open("enc", 'r').read()
flag = ""

for i in range(len(enc)):
    flag += chr((ord(enc[i]) >> 8))
    flag += chr(enc[i].encode("UTF-16BE")[-1])

print(flag)
