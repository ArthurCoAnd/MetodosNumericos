import math
# Importando Ferramentas
from Ferramentas.título import título
# Importando Funções
from ZeroDeFunções.Funções.f import f
from ZeroDeFunções.Funções.df import df
from ZeroDeFunções.Funções.ddf import ddf

def intervalosVálidos(sf):
	título("Intervalos Válidos", '=')
	pos = float(input("Posição INICIAL de Análise : "))
	posF = float(input("Posição FINAL de Análise : "))
	delta = float(input("Tamanho Entre os Intervalos : "))
    # intVal - Contador de Intervalos Válidos
	intVal = 1
	print("")
	while((pos+delta)<posF):
		if((f(pos,sf)*f(pos+delta,sf))<0):
			print("%i-[%f]:[%f]"%(intVal, pos, (pos+delta)))
			intVal += 1
		pos += delta