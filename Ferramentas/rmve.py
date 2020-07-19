def rmve(s):
    r = ""
    tam = len(s)
    p = 0
    while(p<tam):
        if(s[p]=="\n"):
            p += 1
            continue
        else:
            r += s[p]
        p += 1
    return r