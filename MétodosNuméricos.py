import math
from Ferramentas.pedirInt import pedirInt
from Ferramentas.título import título
import ZeroDeFunções.ZeroDeFunções as zdf

def printMenu():
	título("Menu Aplicativo de Métodos Numéricos", '=')
	print("1 - Zero de Funções")
	print("0 - Fechar Programa")

def menu():
    escolha = -1
    while(escolha!=0):
        printMenu()
        escolha = pedirInt(chave=False,s="Escolha")
        if(escolha==1):
            zdf.menu()
        else:
            título("ERRO - Escolha INVÁLIDA", '*')

menu()