# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
# Importando Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.tratamentoSf import tratamentoSf as tSf
from ZeroDeFunções.FerramentasZDF.DadosZDF import dados as d
from ZeroDeFunções.FerramentasZDF.CalcularE import calcularE as cE

def newtonRaphson(d):
	título("Newton-Raphson", '=')

	# Definição das Variaveis Inicias
		# Precisão
	mm.dps = d.dec
	xkAtual = mm.mpf(0.0)
	xkProx = mm.mpf(d.a)
	e = mm.mpf(d.e)
	k = 0
	kmax = (d.kmax-1)
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
	sdf = tSf(d.sdf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(xkAtual,xkProx,e,k,kmax,sf,sdf,resultados)
	tabelaResultados = pd.DataFrame(resultados,columns=["xk","f(xk)","e"])
	print(tabelaResultados)
	print("\n")
	print(s)
	return s
	

def metodo(xkAtual,xkProx,e,k,kmax,sf,sdf,r):
	# Calculos de Variaveis
	s = ""
	xkAtual = xkProx
	fxkA = f(xkAtual,sf)
	dfxkA = f(xkAtual,sdf)
	xkProx = xkAtual - (fxkA/dfxkA)
	fxkP = f(xkProx,sf)
	ek = mm.mpf(cE(sf,xkAtual,xkProx,xkProx))

	# Registrar Resultados
	r[k].append(xkAtual)
	r[k].append(fxkA)
	r[k].append(ek)
	
	# Recursividade
	if((ek>e) and (k<kmax)):
		k+=1
		r.append([])
		s = metodo(xkAtual,xkProx,e,k,kmax,sf,sdf,r)
	else:
		s = ("Newton-Raphson\nInterações\t=\t"+str(k+1)+"\nRaiz\t\t=\t"+str(xkProx)+"\nFunção da Raiz\t=\t"+str(fxkP)+"\ne de parada\t=\t"+str(ek))

	return s