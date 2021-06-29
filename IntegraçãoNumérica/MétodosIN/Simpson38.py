# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN

def Simpson38(dIN):
	# Definir Dados
		# Precisão
	pDec = dIN.pDec
	mm.mp.dps = pDec
		# Tratamento das String de Função
	sf = tSf(dIN.sf)
	sdf = tSf(dIN.sdf)
		# Dados de Análise
	a = mm.mpf(dIN.a)
	b = mm.mpf(dIN.b)
	m = int(dIN.m)
	if(dIN.c == ""):
		c = mm.mpf((b+a)/2)
	else:
		c = mm.mpf(dIN.c)
	h = mm.mpf((b-a)/m)
	
	# Cálculo da Integral
	I = mm.mpf('0')
	for i in range(m):
		xi = mm.mpf(a+(i*h))
		if(i==0 or i==m):
			I += mm.mpf(f((xi),sf,pDec))
		elif(i%3==1 or i%3==2):
			I += mm.mpf(3*f((xi),sf,pDec))
		else:
			I += mm.mpf(2*f((xi),sf,pDec))
	I = mm.mpf((3*h/8)*I)
	
	E = mm.mpf('0')
	# Calculo do Erro
	if(dIN.vc==1):
		E = mm.mpf((3/80)*mm.power(h,5)*f(c,sdf,pDec))

	# Gerar e Retornar Resposta
	resp = ""
	if(dIN.vc==1):
		resp += ("3/8 de Simpson\n\nI = "+str(I)+" ± "+str(E))
		resp += ("\n\nI+E = "+str(mm.mpf(I+E)))
		resp += ("\nI-E = "+str(mm.mpf(I-E)))
	else:
		resp += ("3/8 de Simpson\n\nI = "+str(I))
	return resp