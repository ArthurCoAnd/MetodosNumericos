from math import *
from Ferramentas.tiraCirco import tiraCirco as tC
from Ferramentas.log2log import log2log as l2l
from Ferramentas.vezesX import vezesX as vX

def f(x,s="x"):
    #s = vX(s)
    s = tC(s)
    s = l2l(s)
    y = eval(s)
    return y