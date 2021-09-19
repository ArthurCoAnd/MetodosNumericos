# Importar Bibliotecas
from numpy import zeros
# Importar Ferramentas
from Ferramentas.FatorarMatriz import FatorarMatriz as FM

def FunçãoLinear(p):
	pap = "Função Linear\n\n"
	
	np = len(p)
	# Gerar Matriz Base de Análise
	mat = zeros((2,3))
	# Registrando Parte Esquerda da Igualdade da Matriz
	for l in range(0,2):
		for c in range(0,2):
			for k in range(0,np):
				mat[l][c] += (p[k][0]**l)*(p[k][0]**c)
	# Registrando Parte Direita da Igualdade da Matriz
	for l in range(0,2):
		for k in range(0,np):
			mat[l][2] += p[k][1]*(p[k][0]**l)
	# Fatorar Matriz Base de Análise
	mat = FM(mat)[0]
	# Calcular Coeficientes
	b = mat[1][2]/mat[1][1]
	a = (mat[0][2]-(mat[0][1]*b))/mat[0][0]

	print(pap)

	# Retornar String da Função
	return f"{a} {b:+}x"