from struct import pack

def char(c):
    return pack('=c', c.encode('ascii'))


def word(c):
    return pack('=h', c)


def dword(c):
    return pack('=l', c)

def color(r, g, b):
    return bytes([b, g, r])
