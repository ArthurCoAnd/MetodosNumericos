import math
from Ferramentas.título import título

# Função Para Pedir Número Inteiro
def pedirInt(chave=False ,st="Definir", s="Número Inteiro"):
	if(chave):
		título(st+" "+s, '=')
	x = int(input(s+" : "))
	return x