#!/usr/bin/python3

while True:
    cmd = raw_input("> ")
    lst = []
    for c in cmd:
        if ord('a') <= ord(c) <= ord('z'):
            lst.append( "$\'\\" + oct(ord(c))[1::] + "\'" )
        else:
            lst.append( c )
    print( ''.join(lst) )
