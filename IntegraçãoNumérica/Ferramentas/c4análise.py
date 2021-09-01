# Importar Bilbiotecas
from numpy import linspace
# Imporatar Ferramentas
from Ferramentas.f import f

def c4análise(a,b,sf):
    c = linspace(a,b,10000)
    maior = 0
    pmaior = 0
    for i in range(len(c)):
        fc = abs(f(c[i],sf))
        if fc > maior:
            maior = fc
            pmaior = i
    return f(c[pmaior],sf)
