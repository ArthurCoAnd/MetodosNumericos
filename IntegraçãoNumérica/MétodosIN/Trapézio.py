# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN

def Trapézio(dIN):
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
	c = mm.mpf(dIN.c)
	h = mm.mpf((b-a)/m)
	
	# Cálculo da Integral
	I = mm.mpf('0')
	for i in range(m):
		xi = mm.mpf(a+(i*h))
		if(i==0 or i==m):
			I += mm.mpf(f((xi),sf,pDec))
		else:
			I += mm.mpf(2*f((xi),sf,pDec))
	I = mm.mpf((h/2)*I)
	
	E = mm.mpf('0')
	# Calculo do Erro
	if(dIN.vc==1):
		E = mm.mpf((mm.power(h,3)/12)*f(c,sdf,pDec))

	# Gerar e Retornar Resposta
	resp = ""
	if(dIN.vc==1):
		resp += ("Trapézio\n\nI = "+str(I)+" ± "+str(E))
		resp += ("\n\nI+E = "+str(mm.mpf(I+E)))
		resp += ("\nI-E = "+str(mm.mpf(I-E)))
	else:
		resp += ("Trapézio\n\nI = "+str(I))
	return resp