import sys

name = sys.argv[1]

f = open(name, "rb")
o = open(name + "_cracked", "wb")
try:
    byte = f.read(1)
    while len(byte)>0:
        re = 255 - ord(byte)
        o.write(re.to_bytes(1, byteorder='big'))
        byte = f.read(1)
finally:
    f.close()
    o.close()
