# Importar Bibliotecas
from math import *

def erro(a,b,fx):
	dif = abs(b-a)
	if(dif<abs(fx)):
		erro = dif
	else:
		erro = abs(fx)
	return erro