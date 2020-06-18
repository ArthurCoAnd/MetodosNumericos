import math
# Importando Ferramentas
from Ferramentas.título import título
# Importando Funções
from ZeroDeFunções.Funções.f import f

def pontoFixo(a,b,e,kmax,sf,spf):
	título("Ponto Fixo", '=')
	xk=a
	xkm=0
	k = 1
	print("%-5s%-10s%-10s%-10s\n"%("K","xk","e","f(xk)"))
	while( (abs(xk-xkm) > e) and (k<=kmax) ):
		xkm=xk
		xk = f(xkm,spf)
		print("%-5d%-10f%-10f%-10f\n"%(k,xk,abs(xk-xkm),f(xk,sf)))
		k+=1
	print("\nRaiz:%f \t f(raiz)=%f \t Erro Final:%f\n\n"%(xk,f(xk,sf),abs(xk-xkm)))