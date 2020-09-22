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
	pDec = d.dec
	mm.mp.dps = pDec
	mm.mp.trap_complex = True
	xkAtual = mm.mpf('0.0')
	xkProx = mm.mpf(d.a)
	e = mm.mpf(d.e)
	k = 0
	kmax = (int(d.kmax)-1)
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
	sdf = tSf(d.sdf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(xkAtual,xkProx,e,k,kmax,sf,sdf,resultados,pDec)
	tabelaResultados = pd.DataFrame(resultados,columns=["xk","f(xk)","e","xk+1"])
	print(tabelaResultados)
	print("\n")
	print(s)
	return s
	

def metodo(xkAtual,xkProx,e,k,kmax,sf,sdf,r,pDec):
	# Calculos de Variaveis
	s = ""
	xkAtual = xkProx
	fxkA = f(xkAtual,sf,pDec)
	dfxkA = f(xkAtual,sdf,pDec)
	xkProx = xkAtual - (fxkA/dfxkA)
	ek = mm.mpf(cE(sf,xkAtual,xkProx,xkAtual,pDec))

	# Registrar Resultados
	r[k].append(xkAtual)
	r[k].append(fxkA)
	r[k].append(ek)
	r[k].append(xkProx)
	
	# Recursividade
	if((ek>e) and (k<kmax)):
		k+=1
		r.append([])
		s = metodo(xkAtual,xkProx,e,k,kmax,sf,sdf,r,pDec)
	else:
		s = ("Newton-Raphson\nInterações\t=\t"+str(k+1)+"\nRaiz\t\t=\t"+str(xkAtual)+"\nFunção da Raiz\t=\t"+str(fxkA)+"\ne de parada\t=\t"+str(ek))

	return s