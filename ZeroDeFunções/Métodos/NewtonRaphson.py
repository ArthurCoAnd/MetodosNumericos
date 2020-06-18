import math
# Importando Ferramentas
from Ferramentas.título import título
# Importando Funções
from ZeroDeFunções.Funções.f import f

def newtonRaphson(a,e,kmax,sf,sdf):
	título("Newton-Raphson", '=')
	xk=a
	xkAnt=999
	k=1
	print("%-5s%-12s%-12s%-12s%-12s%-12s"%("K","xk","f(xk)","f'(xk)","xk+1","e"))
	while( (abs(xk-xkAnt)>e) and k<=kmax ):
		xkAnt=xk
		xk = xkAnt - (f(xkAnt,sf)/f(xkAnt,sdf))
		print("%-5d%-12f%-12f%-12f%-12f%-12f"%(k,xkAnt,f(xkAnt,sf),f(xkAnt,sdf),xk,abs(xk-xkAnt)))
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),abs(xk-xkAnt)))