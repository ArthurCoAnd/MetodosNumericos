import math
# Importando Ferramentas
from Ferramentas.título import título
from Ferramentas.pedirInt import pedirInt
from Ferramentas.pedirIntPos import pedirIntPos
from Ferramentas.pedirFloat import pedirFloat
from Ferramentas.pedirFloatMaiorQue import pedirFloatMaiorQue

def menuDados():
	título("Menu de Gerenciamento de Dados - Ajuste de Funções", '=')
	print("1 - Registrar Novos Pontos")
	print("2 - Alterar Ponto")
	print("0 - Voltar")