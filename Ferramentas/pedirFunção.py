import math
from Ferramentas.título import título
import ZeroDeFunções.MenuDados as F

# Função Para Pedir String da Função
def pedirFunção(chave=False ,st="Definir", s="Função"):
	if(chave):
		título(st+" "+s, '=')
	x=""
	x = input(s+" : ")
	return x