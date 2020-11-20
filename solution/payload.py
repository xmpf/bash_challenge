#!/usr/bin/python3

USE_UNICODE=True

while True:
    cmd = input("> ")
    lst = ["$'"]
    for c in cmd:
        cc = ord(c)
        if ord('a') <= cc <= ord('z'):
            lst.append( "\\U{:x}".format(cc) if USE_UNICODE else f"\\{oct(cc)[2:]}" )
        else:
            lst.append( c )
    lst.append( "'" )
    print( ''.join(lst) )
