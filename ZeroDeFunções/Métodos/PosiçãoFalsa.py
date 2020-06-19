import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
# Importando Funções
from ZeroDeFunções.Funções.f import f

def posiçãoFalsa(a,b,e,kmax,sf):
	título("Posição Falsa", '=')
	k = 1
	xkAnt = 0
	xk = (a*abs(f(b,sf)) + b*abs(f(a,sf))) / (abs(f(a,sf)) + abs(f(b,sf)))
	print("%-5s%-12s%-12s%-12s%-12s%-12s%-12s%-12s"%("K","A","xk","B","e","f(a)","f(xk)","f(b)"))
	while((calcularErro(sf,a,b,xk)>e) and (k<=kmax)):
		xkAnt = xk
		xk = (a*abs(f(b,sf)) + b*abs(f(a,sf))) / (abs(f(a,sf)) + abs(f(b,sf)))
		print("%-5d%-12f%-12f%-12f%-12f%-12f%-12f%-12f"%(k,a,xk,b,calcularErro(sf,a,b,xk),f(a,sf),f(xk,sf),f(b,sf)))
		if ( f(a,sf) * f(xk,sf) < 0 ):
			b = xk
		else:
			a = xk
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),calcularErro(sf,a,b,xk)))