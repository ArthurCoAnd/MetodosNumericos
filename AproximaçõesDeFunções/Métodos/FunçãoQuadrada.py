# Importar Bibliotecas
from numpy import matrix, zeros
# Importar Ferramentas
from Ferramentas.FatorarMatriz import FatorarMatriz as FM

def FunçãoQuadrada(p):
	pap = "Função Quadrada\n\n"
	
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
	pap += f"Matriz:\n{str(matrix(mat))}"
	# Fatorar Matriz Base de Análise
	mat = FM(mat)[0]
	pap += f"\n\nMatriz Fatorada:\n{str(matrix(mat))}"
	# Calcular Coeficientes
	a = mat[2][3]/mat[2][2]
	b = (mat[1][3]-(mat[1][2]*a))/mat[1][1]
	c = (mat[0][3]-(mat[0][1]*b)-(mat[0][2]*a))/mat[0][0]
	pap += f"\n\nCoeficiente a: {a}"
	pap += f"\nCoeficiente b: {b}"
	pap += f"\nCoeficiente c: {c}"

	resp = f"{a:.7}*x^2 {b:+.7}*x {c:+.7}"
	pap += f"\n\nAproximação: {resp}"
	print(pap)

	# Retornar String da Função
	return resp, pap