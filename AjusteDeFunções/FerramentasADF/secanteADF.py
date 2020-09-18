# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
# Importando Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.tratamentoSf import tratamentoSf as tSf
from ZeroDeFunções.FerramentasZDF.CalcularE import calcularE as cE

def secanteADF(xkA,xkP,sf,prec):
	título("Secante", '=')

	# Definição das Variaveis Inicias
		# Precisão
	mm.dps = prec
	xkAtual = mm.mpf(xkA)
	xkProx = mm.mpf(xkP)
	e = mm.mpf('10e-(prec-2)')
	k = 0
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	resposta = metodo(xkAtual,xkProx,e,k,kmax,sf,resultados)
	tabelaResultados = pd.DataFrame(resultados,columns=["xk","f(xk)","e"])
	print(tabelaResultados)
	return resposta
	
def metodo(xkAtual,xkProx,e,k,sf,r):
	# Calculos de Variaveis
	s = ""
	fxkA = f(xkAtual,sf)
	fxkP = f(xkProx,sf)
	xkProxProx = ( (xkAtual*fxkP) - (xkProx*fxkA) ) / ( fxkP - fxkA )
	ek = mm.mpf(cE(sf,xkAtual,xkProx,xkProx))

	# Registrar Resultados
	r[k].append(xkAtual)
	r[k].append(fxkA)
	r[k].append(ek)
	
	# Recursividade
	if(ek>e):
		k+=1
		r.append([])
		s = metodo(xkProx,xkProxProx,e,k,sf,r)
	else:
		print("Secante\nInterações\t=\t"+str(k+1)+"\nRaiz\t\t=\t"+str(xkProx)+"\nFunção da Raiz\t=\t"+str(fxkP)+"\ne de parada\t=\t"+str(ek))

	return xkAtual