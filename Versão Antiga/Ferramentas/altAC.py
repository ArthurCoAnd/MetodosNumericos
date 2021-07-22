'''
altAC - Alterador de Acentos Circunflexos

Altera o Char '^' por "**"
	ex: "4*x^3" -> "4*x**3"
'''
def altAC(s):
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