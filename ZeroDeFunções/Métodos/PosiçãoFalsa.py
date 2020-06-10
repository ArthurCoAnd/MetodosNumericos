import math
# Importando Ferramentas
from Ferramentas.título import título
# Importando Funções
from ZeroDeFunções.Funções.f import f

def posiçãoFalsa(a,b,e,kmax,sf):
	título("Posição Falsa", '=')
	k = 1
	xkAnt = 0
	xk = (a*abs(f(b,sf)) + b*abs(f(a,sf))) / (abs(f(a,sf)) + abs(f(b,sf)))
	print("%-5s%-12s%-12s%-12s%-12s%-12s%-12s%-12s"%("K","A","xk","B","f(a)","f(xk)","f(b)","e"))
	while((abs(f(xk,sf))>e or abs(xk-xkAnt)>e) and (k<=kmax)):
		xkAnt = xk
		xk = (a*abs(f(b,sf)) + b*abs(f(a,sf))) / (abs(f(a,sf)) + abs(f(b,sf)))
		print("%-5d%-12f%-12f%-12f%-12f%-12f%-12f%-12f"%(k,a,xk,b,f(a,sf),f(xk,sf),f(b,sf),abs(xk-xkAnt)))
		if ( f(a,sf) * f(xk,sf) < 0 ):
			b = xk
		else:
			a = xk
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),abs(xk-xkAnt)))