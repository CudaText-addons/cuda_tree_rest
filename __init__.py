def is_head(ln,sym):
    if ln=='':
        return False
    for i in ln:
        if not i==sym:
            return False
    return True

def is_arr(ln):
    arr='-=\'"`:^~_*+#<>'
    for i in arr:
        if is_head(ln,i):
            return True
    return False
    
def lvl(s):
    if s=='=':
        return 1
    elif s=='-':
        return 2
    elif s=='~':
        return 3
    elif s=='"':
        return 4
    return 1

def get_headers(filename, lines):
    '''
    Gets tuples in format
    ((x1, y1, x2, y2), level, title, icon)
    '''
    r = []
    for n,i in enumerate(lines):
        if is_arr(i):
            if n>0:
                if 0<len(lines[n-1])<=len(i):
                    r.append( ((0, n-1, 0, n), lvl(i[0]), lines[n-1], -1) )
    return r
