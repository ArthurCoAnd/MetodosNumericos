from Ferramentas.título import título

def printMenuDados(sf,sdf,sddf,a,b,e,kmax):
	título("Menu Gerenciamento de Dados Zero De Funções", '=')
	printDadosAtuais(sf,sdf,sddf,a,b,e,kmax)
	print("1 - Definir Todos os Dados")
	print("2 - Definir Função")
	print("3 - Definir Função Derivada Primeira")
	print("4 - Definir Função Derivada Segunda")
	print("5 - Definir Intervalo")
	print("6 - Definir Erro")
	print("7 - Definir Máximo de Interações")
	print("8 - Intervalos Válidos")
	print("9 - Verifar Intervalo Atual")
	print("0 - Voltar")

def printDadosAtuais(sf,sdf,sddf,a,b,e,kmax):
	printFunções(sf,sdf,sddf)
	print("Dados Atuais:")
	printIntervalo(a,b)
	printErro(e)
	printInteraçõesMáxima(kmax)
	print("")

def printFunções(sf,sdf,sddf):
	print("Funções Atuais:")
	printF(sf)
	printDF(sdf)
	printDDF(sddf)
	print("")

def printF(sf):
	print("%-20s - %s"%("f(x)",sf))

def printDF(sdf):
	print("%-20s - %s"%("df(x)",sdf))

def printDDF(sddf):
	print("%-20s - %s"%("ddf(x)",sddf))

def printIntervalo(a,b):
	print("%-20s - [%f]:[%f]"%("Intervalo Atual",a,b))

def printErro(e):
	print("%-20s - %f"%("Erro Atual",e,))

def printInteraçõesMáxima(kmax):
	print("%-20s - %i"%("Máximo de Interações",kmax))
