#!/usr/bin/python3

while True:
    cmd = input("> ")
    lst = []
    for c in cmd:
        if ord('a') <= ord(c) <= ord('z'):
            lst.append( "$\'\\" + oct(ord(c))[2::] + "\'" )
        else:
            lst.append( c )
    print( ''.join(lst) )
