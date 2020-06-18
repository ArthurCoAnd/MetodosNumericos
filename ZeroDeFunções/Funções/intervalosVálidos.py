import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
# Importando Funções
from ZeroDeFunções.Funções.f import f

def intervalosVálidos(sf,sdf):
	título("Intervalos Válidos", '=')
	pos = pedirFloat(s="Posição INICIAL de Análise")
	posF = pedirFloatMaiorQue(pos, s="Posição FINAL de Análise")
	delta = pedirFloat(s="Tamanho Entre os Intervalos")
    # intVal - Contador de Intervalos Válidos
	intVal = 1
	print("")

	while((pos+delta)<posF):
		if( ((f(pos,sf)*f(pos+delta,sf))<0) and (f(pos,sdf)*f(pos+delta,sdf)>0) ):
			print("%i-[%f]:[%f]"%(intVal, pos, (pos+delta)))
			intVal += 1
		pos += delta