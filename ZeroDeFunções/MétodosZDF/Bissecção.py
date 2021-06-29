# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
# Importando Ferramentas
from Ferramentas.f import f
from Ferramentas.título import título
from Ferramentas.tratamentoSf import tratamentoSf as tSf
from ZeroDeFunções.FerramentasZDF.DadosZDF import dados as d
from ZeroDeFunções.FerramentasZDF.RespostaZDF import RespostaZDF as rZDF
from ZeroDeFunções.FerramentasZDF.CalcularE import calcularE as cE

def bissecção(d):
	título("Bissecçâo", '=')
	
	# Definição das Variaveis Inicias
		# Precisão
	pDec = d.dec
	mm.mp.dps = pDec
	mm.mp.trap_complex = True
	a = mm.mpf(d.a)
	b = mm.mpf(d.b)
	e = mm.mpf(d.e)
	k = 0
	kmax = (int(d.kmax)-1)
		# Tratamento das Strings de Funções
	sf = tSf(d.sf)
		# Matriz com dos resultados
	resultados = [[]]

	# Calculos
	s = metodo(a,b,e,k,kmax,sf,resultados,pDec)
	tabelaResultados = pd.DataFrame(resultados,columns=["A","xk","B","e","f(a)","f(xk)","(fb)"])
	print(tabelaResultados)
	print("\n")
	print(s)

	resp = rZDF(s,str(tabelaResultados))
	
	return resp
	

def metodo(a,b,e,k,kmax,sf,r,pDec):
	# Calculos de Variaveis
	s   = ""
	xk  = mm.mpf((b+a)/2)
	ek  = mm.mpf(cE(sf,a,b,xk,pDec))
	fa  = f(a,sf,pDec)
	fxk = f(xk,sf,pDec)
	fb  = f(b,sf,pDec)

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
		s = metodo(a,b,e,k,kmax,sf,r,pDec)
	else:
		s = ("Método da Bissecção:\nNúmero de Iterações\t=\t"+str(k+1)+"\nRaiz da Função f(ẋ)\t=\t"+str(xk)+"\nValor f(ẋ)\t\t=\t"+str(fxk)+"\nErro\t\t\t=\t"+str(ek))

	return s