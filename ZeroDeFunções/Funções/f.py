from math import *
# Importar Ferramentas
from Ferramentas.altAC import altAC as aAC
from Ferramentas.log2log import log2log as l2l
from Ferramentas.vezesX import vezesX as vX

# f - Função
def f(x,s="x"):
    #s = vX(s)
    s = aAC(s)
    s = l2l(s)
    y = eval(s)
    return y