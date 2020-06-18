import math
from Ferramentas.pedirInt import pedirInt
from Ferramentas.título import título
import ZeroDeFunções.ZeroDeFunções as zdf
import AjusteDeFunções.AjusteDeFunções as adf

def printMenu():
	título("Menu Aplicativo de Métodos Numéricos", '=')
	print("1 - Zero de Funções")
	#print("3 - Ajuste de Funções")
	print("0 - Fechar Programa")

def menu():
	escolha = -1
	while(escolha!=0):
		printMenu()
		escolha = pedirInt(s="Escolha")
		if(escolha==1):
			zdf.menu()
		#if(escolha==3):
		#	adf.menu()
		elif(escolha==0):
			escolha=0
		else:
			título("ERRO - Escolha INVÁLIDA", '*')

menu()