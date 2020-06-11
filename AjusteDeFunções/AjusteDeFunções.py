import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirInt import pedirInt
from Ferramentas.pedirIntPos import pedirIntPos
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue
# Importando
import AjusteDeFunções.MenuDados as MD

def printMenu():
	título("Menu Ajuste de Funções", '=')
	print("1 - Gerenciameno de Dados")
	print("2 - Ajustar Funções")
	print("0 - Voltar")

def menu():
	escolha = -1
	while (escolha != 0):
		printMenu()
		escolha = pedirInt(s="Escolha")
		if (escolha==1):
			MD.menuDados()
		elif (escolha==2):
			print("Escolha 2")
		elif (escolha==0):
			escolha==0
		else:
			título("ERRO - Escolha Inválida", '*')