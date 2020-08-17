import math
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.Métodos.CalcularErro import calcularErro
# Importando Funções
from ZeroDeFunções.Funções.f import f

def secanteADF(xk,xkAnt,sf):
	k = 1
	print("%-5s%-12s%-12s%-12s\n"%("K","xk","f(xk)","e"))
	while( (calcularErro(sf,xk,xkAnt,xk)>0.00001) and (k<=100) ):
		aux = xk
		xk = (xkAnt*f(xk,sf)-xk*f(xkAnt,sf))/(f(xk,sf)-f(xkAnt,sf))
		xkAnt = aux
		print("%-5d%-12f%-12f%-12f"%(k,xk,f(xk,sf),calcularErro(sf,xk,xkAnt,xk)))
		k+=1
	print("\nSecante\n%-15s\tk\t=\t%i\n%-15s\tx\t=\t%f\n%-15s\tf(x)\t=\t%f\n%-15s\te\t=\t%f"%("Interações",k-1,"Raiz",xk,"Função da Raiz",f(xk,sf),"Erro",calcularErro(sf,xk,xkAnt,xk)))

	return xk