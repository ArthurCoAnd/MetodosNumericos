from mpmath import *
# f - Função
def f(x,s,pDec=16):
    mp.dps = pDec
    mp.trap_complex = True
    x = mp.mpf(x)
    y = eval(s)
    return y