#!/usr/bin/python3

USE_UNICODE = True          # use UNICODE or OCTAL
    
is_next_safe = False        # if next character is in ['A' .. 'F'] unicode representation should be padded        
while True:
    cmd = input("> ")
    lst = ["$'"]
    cmd_len = len(cmd)
    next_char = ''
    for i in range(cmd_len):
        if i < cmd_len - 1:
            next_char = cmd[i + 1]
        is_next_safe = not( ord('A') <= ord(next_char) <= ord('F') )
        cc = ord(cmd[i])
        if ord('a') <= cc <= ord('z'):
            lst.append( (("\\U{:x}" if is_next_safe else "\\U{:08x}") if USE_UNICODE else "\\{:o}").format(cc) )
        else:
            lst.append( cmd[i] )
    lst.append( "'" )
    print( ''.join(lst) )
