# Importar Ferramentas
from Ferramentas.vezesX import vezesX as vX
from Ferramentas.altAC import altAC as aAC
from Ferramentas.log2log import log2log as l2l
from Ferramentas.esp2Dec import esp2Dec as e2d

# Tratar String de Função
def tratamentoSf(s):
    s = vX(s)
    s = aAC(s)
    s = l2l(s)
    #s = e2d(s)
    return s