# coding: utf-8
import sys

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

def random(size=16):
    '''
    Wikipedia によると、/dev/urandom ("unlocked" random source) は
    暗号論的擬似乱数生成器として機能することを意図しており、それほど安全性を要求されない用途に使う。
    '''
    return open("/dev/urandom").read(size)

def encrypt(key, msg):
    c = strxor(key, msg)
    return c

def decrypt(key, ct):
    m = strxor(key, ct)
    return m

def str2hex(a):
    return a.encode('hex')

def hex2str(a):
    return a.decode('hex')


if __name__ == '__main__':

    m    = "This is a stream cipher test using one time pad.\n" \
           "Never use the same key twice! otherwise it can be easliy broken."
    k    = random(len(m))
    ct   = encrypt(k, m)

    print "-- message --\n" + m
    print "-- secret key --\n" + str2hex(k)
    print "-- cipher text --\n" + str2hex(ct)

    m2   = decrypt(k, ct)
    print "-- decrypted text --\n" + m2


