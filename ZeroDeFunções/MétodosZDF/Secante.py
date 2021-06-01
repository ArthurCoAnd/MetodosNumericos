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
	pDec = d.dec
	mm.mp.dps = pDec
	mm.mp.trap_complex = True
	xkAnterior = mm.mpf('0.0')
	xkAtual = mm.mpf(d.a)
	xkProx = mm.mpf(d.b)
	e = mm.mpf(d.e)
	k = 0
	kmax = (int(d.kmax)-1)
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(xkAnterior,xkAtual,xkProx,e,k,kmax,sf,resultados,pDec)
	tabelaResultados = pd.DataFrame(resultados,columns=["xk","f(xk)","e"])
	print(tabelaResultados)
	print("\n")
	print(s)
	return s
	

def metodo(xkAnterior,xkAtual,xkProx,e,k,kmax,sf,r,pDec):
	# Definição Precisão
	mm.mp.dps = pDec

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
	if((ek>e) and (k<=kmax)):
		k+=1
		r.append([])
		s = metodo(xkAtual,xkProx,xkProxProx,e,k,kmax,sf,r,pDec)
	else:
		s = ("Método da Secante\nNúmero de Interações\t=\t"+str(k)+"\nRaiz da Função f(x)\t=\t"+str(xkAtual)+"\nValor f(Raiz)\t\t=\t"+str(fxkA)+"\nErro\t\t\t=\t"+str(ek))

	return s