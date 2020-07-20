def tiraCirco(s):
    r = ""
    tam = len(s)
    p = 0
    while(p<tam):
        if(s[p]=="^"):
            r += "**"
        else:
            r += s[p]
        p += 1
    return r