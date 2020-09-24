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
	mm.mp.dps = prec
	mm.mp.trap_complex = True
	xkAnterior = mm.mpf('0.0')
	xkAtual = mm.mpf(xkA)
	xkProx = mm.mpf(xkP)
	e = mm.mpf(10**(3-prec))
	k = 0
		# Tratamento das Strings de Funções
	sf = tSf(sf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(xkAnterior,xkAtual,xkProx,e,k,sf,resultados,prec)
	tabelaResultados = pd.DataFrame(resultados,columns=["xk","f(xk)","e"])
	print(tabelaResultados)
	return s
	

def metodo(xkAnterior,xkAtual,xkProx,e,k,sf,r,pDec):
	# Calculos de Variaveis
	s = ""
	fxkA = f(xkAtual,sf,pDec)
	fxkP = f(xkProx,sf,pDec)
	xkProxProx = ( (xkAtual*fxkP) - (xkProx*fxkA) ) / ( fxkP - fxkA )
	ek = mm.mpf(cE(sf,xkAtual,xkAnterior,xkAtual,pDec,k))

	# Registrar Resultados
	r[k].append(xkAtual)
	r[k].append(fxkA)
	r[k].append(ek)
	
	# Recursividade
	if(ek>e):
		k+=1
		r.append([])
		s = metodo(xkAtual,xkProx,xkProxProx,e,k,sf,r,pDec)
	else:
		s = ("Secante\nInterações\t=\t"+str(k+1)+"\nRaiz\t\t=\t"+str(xkAtual)+"\nFunção da Raiz\t=\t"+str(fxkA)+"\ne de parada\t=\t"+str(ek))
		print(s)
		s = xkAtual

	return s