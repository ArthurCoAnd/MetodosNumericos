import math
from Ferramentas.título import título

# Função Para Pedir Número Real Maior que X
def pedirFloatMaiorQue(x, chave=False, st="Definir", s="Número Real Mairo Que"):
	if(chave):
		título(st+" "+s, '=')
	y = x-1.0
	while (y<=x):
		y = float(input(s+" : "))
		if (y<=x):
			título("ERRO - Escolha Inválida", '*')
	return y