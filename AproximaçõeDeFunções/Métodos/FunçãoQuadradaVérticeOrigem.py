def FunçãoQuadradaVérticeOrigem(p):
	np = len(p)
	# Calcular Coeficientes
	somaX2Y = 0
	somaX4 = 0
	for i in range(np):
		somaX2Y += (p[i][0]**2)*(p[i][1])
		somaX4 += p[i][0]**4
	a = somaX2Y/somaX4
	# Retornar String da Função
	return f"{a}*x^2"