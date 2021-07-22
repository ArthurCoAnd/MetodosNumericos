# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas

def MatrizIdentidade(tam, prec):
	# Precisão Dígitos
	mm.mp.dps = prec

	# Matriz Identidade
	matId = []

	for l in range (tam):
		matId.append([])
		for c in range (tam):
			if(l==c):
				matId[l].append(mm.mpf('1'))
			else:
				matId[l].append(mm.mpf('0'))
	
	return matId