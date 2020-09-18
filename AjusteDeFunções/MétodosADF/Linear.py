# Importar Bibliotecas
import mpmath as mm 
import pandas as pd
# Importar Ferramentas
from Ferramentas.título import título

def linear(raiz):
	título("Função Linear", "=")
	print("Matriz Base:")
	print("f(x) = a + bx")

	# Ler Dados
	pts = raiz.lerDados()

	# Gerar Matriz Base de Análise
	mat = [[0.0,0.0,0.0],[0.0,0.0,0.0]]
		# Registrando Parte Esquerda da Igualdade da Matriz
	for l in range (0,2):
		for c in range (0,2):
			for k in range (0,raiz.n):
				mat[l][c] += ((pts[0][k])**l)*((pts[0][k])**c)	
		# Registrando Parte Direita da Igualdade da Matriz
	for l in range (0,2):
		for k in range (0,raiz.n):
			mat[l][2] += pts[1][k]*(pts[0][k]**l)
		# Print Matriz Base de Análise
	print("\nMatriz Base:")
	raiz.printMat(mat)

	# Fatorar Matriz Base de Análise
	raiz.fatorarMat(mat)
	print("\nMatriz Base Fatorada:")
	raiz.printMat(mat)

	# Processar Dados Finais
	b = mat[1][2]/mat[1][1]
	a = (mat[0][2]-(mat[0][1]*b))/mat[0][0]

	# Gerar Resposta
	print("\nFunção Aproximada:")
	print("f(x) = %f + %fx"%(a,b))
	s = ""
	s += "Função Linear Base:\n"
	s += "f(x) = a + bx\n"
	s += "Ajuste Encontrado:\n"
	s += "f(x) = %f + %fx"%(a,b)
	raiz.jResposta.txtResp = s
	raiz.jResposta.texto.config(text=raiz.jResposta.txtResp)

	# Finalizar
	raiz.jResposta.sf = "%f+%f*x"%(a,b)
	raiz.jResposta.opçõesRespostas()