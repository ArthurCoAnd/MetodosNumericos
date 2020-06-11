import math
from Ferramentas.título import título

# Função Para Pedir Número Inteiro
def pedirFloat(chave=False, st="Definir", s="Número Real"):
	if(chave):
		título(st+" "+s, '=')
	x = float(input(s+" : "))
	return x