# Importar Bibliotecas
from numpy import zeros
# Importar Ferramentas
from Ferramentas.FatorarMatriz import FatorarMatriz as FM

def FunçãoQuadrada(p):
	np = len(p)
	# Gerar Matriz Base de Análise
	mat = zeros((3,4))
	# Registrando Parte Esquerda da Igualdade da Matriz
	for l in range(0,3):
		for c in range(0,3):
			for k in range(0,np):
				mat[l][c] += (p[k][0]**l)*(p[k][0]**c)
	# Registrando Parte Direita da Igualdade da Matriz
	for l in range(0,3):
		for k in range(0,np):
			mat[l][3] += (p[k][1])*(p[k][0]**l)
	# Fatorar Matriz Base de Análise
	mat = FM(mat)[0]
	# Calcular Coeficientes
	a = mat[2][3]/mat[2][2]
	b = (mat[1][3]-(mat[1][2]*a))/mat[1][1]
	c = (mat[0][3]-(mat[0][1]*b)-(mat[0][2]*a))/mat[0][0]
	# Retornar String da Função
	return f"{a}*x^2 {b:+}*x {c:+}"