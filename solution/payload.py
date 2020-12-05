#!/usr/bin/python3

USE_UNICODE = True          # use UNICODE or OCTAL
# if next character is in ['A' .. 'F'] unicode representation should be padded 

escape = lambda x: f'\{x}' if x in ['\'', '\\'] else x

while True:
    is_next_safe = True       
    cmd = input("> ")
    lst = ["$'"]
    cmd_len = len(cmd)
    next_char = ''
    for ix, c in enumerate(cmd):
        if ix < cmd_len - 1:
            next_char = cmd[ix + 1]
            is_next_safe = not( ord('A') <= ord(next_char) <= ord('F') )
        cc = ord(c)
        if ord('a') <= cc <= ord('z'):
            lst.append( (("\\U{:x}" if is_next_safe else "\\U{:08x}") \
                if USE_UNICODE else "\\{:o}").format(cc) )
        else:
            lst.append( escape(c) )
    lst.append( "'" )
    print( ''.join(lst) )
