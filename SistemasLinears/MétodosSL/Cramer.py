# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.fatorarMatriz import fatorarMatriz as fM

def Cramer(mat, prec):
	resp = "Botão Apertado"
	mm.mp.dps = prec
	nV = len(mat)
	print("Matriz\n"+str(mm.matrix(mat)))
	mat = fM(mat,prec)
	print("Matriz Fatorada\n"+str(mm.matrix(mat)))

	return resp