import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
# Importando Funções
from ZeroDeFunções.Funções.f import f

def pontoFixo(a,b,e,kmax,sf,spf):
	título("Ponto Fixo", '=')
	xk=a
	xkAnt=b
	k = 1
	print("%-5s%-10s%-10s%-10s"%("K","xk","e","f(xk)"))
	while( (calcularErro(sf,xk,xkAnt,xk)>e) and (k<=kmax) ):
		xkAnt=xk
		xk = f(xkAnt,spf)
		print("%-5d%-10f%-10f%-10f"%(k,xk,calcularErro(sf,xk,xkAnt,xk),f(xk,sf)))
		k+=1

	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),calcularErro(sf,xk,xkAnt,xk)))