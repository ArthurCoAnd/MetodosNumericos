import math
from Ferramentas.título import título
import ZeroDeFunções.ZeroDeFunções as zdf

def printMenu():
	título("Menu Aplicativo de Métodos Numéricos", '=')
	print("1 - Zero de Funções")
	print("0 - Fechar Programa")

def menu():
    printMenu()
    escolha = -1
    escolha = int(input("Escolha : "))
    while(escolha!=0):
        if(escolha==1):
            zdf.menu()
        else:
            título("ERRO - Escolha INVÁLIDA", '*')

menu()