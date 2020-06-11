import math
from Ferramentas.título import título

# Função Para Pedir Número Inteiro Positivo
def pedirIntPos(chave=False, st="Definir", s="Número Inteiro Positivo"):
	if(chave):
		título(st+" "+s, '=')
	x = -1
	while (x <=0):
		x = int(input(s+" : "))
		if (x <=0):
			título("ERRO - Escolha Inválida", '*')
	return x