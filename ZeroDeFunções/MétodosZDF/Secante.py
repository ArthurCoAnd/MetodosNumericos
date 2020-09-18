# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
# Importando Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.tratamentoSf import tratamentoSf as tSf
from ZeroDeFunções.FerramentasZDF.DadosZDF import dados as d
from ZeroDeFunções.FerramentasZDF.CalcularE import calcularE as cE

def secante(d):
	título("Secante", '=')

	# Definição das Variaveis Inicias
		# Precisão
	mm.dps = d.dec
	xkAtual = mm.mpf(d.a)
	xkProx = mm.mpf(d.b)
	e = mm.mpf(d.e)
	k = 0
	kmax = (d.kmax-1)
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(xkAtual,xkProx,e,k,kmax,sf,resultados)
	tabelaResultados = pd.DataFrame(resultados,columns=["xk","f(xk)","e"])
	print(tabelaResultados)
	print("\n")
	print(s)
	return s
	

def metodo(xkAtual,xkProx,e,k,kmax,sf,r):
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
	if((ek>e) and (k<kmax)):
		k+=1
		r.append([])
		s = metodo(xkProx,xkProxProx,e,k,kmax,sf,r)
	else:
		s = ("Secante\nInterações\t=\t"+str(k+1)+"\nRaiz\t\t=\t"+str(xkProx)+"\nFunção da Raiz\t=\t"+str(fxkP)+"\ne de parada\t=\t"+str(ek))

	return s