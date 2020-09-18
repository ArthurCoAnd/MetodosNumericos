# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
# Importando Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.tratamentoSf import tratamentoSf as tSf
from ZeroDeFunções.FerramentasZDF.DadosZDF import dados as d
from ZeroDeFunções.FerramentasZDF.CalcularE import calcularE as cE

def posiçãoFalsa(d):
	título("Posição Falsa", '=')
	
	# Definição das Variaveis Inicias
		# Precisão
	mm.dps = d.dec
	a = mm.mpf(d.a)
	b = mm.mpf(d.b)
	e = mm.mpf(d.e)
	k = 0
	kmax = (d.kmax-1)
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(a,b,e,k,kmax,sf,resultados)
	tabelaResultados = pd.DataFrame(resultados,columns=["A","xk","B","e","f(a)","f(xk)","f(b)"])
	print(tabelaResultados)
	print("\n")
	print(s)
	return s

def metodo(a,b,e,k,kmax,sf,r):
	# Calculos de Variaveis
	s   = ""
	fa  = f(a,sf)
	fb  = f(b,sf)
	xk = (a*abs(fb) + b*abs(fa)) / (abs(fa) + abs(fb))
	fxk = f(xk,sf)
	ek  = mm.mpf(cE(sf,a,b,xk))

	# Registrar Resultados
	r[k].append(a)
	r[k].append(xk)
	r[k].append(b)
	r[k].append(ek)
	r[k].append(fa)
	r[k].append(fxk)
	r[k].append(fb)

	# Definir Próximo Intervalo de Análise
	if ((fa*fxk)<0):
		b = xk
	else:
		a = xk

	# Recursividade
	if((ek>e) and (k<kmax)):
		k+=1
		r.append([])
		s = metodo(a,b,e,k,kmax,sf,r)
	else:
		s = ("Posição Falsa\nInterações\t=\t"+str(k+1)+"\nRaiz\t\t=\t"+str(xk)+"\nFunção da Raiz\t=\t"+str(fxk)+"\ne de parada\t=\t"+str(ek))

	return s