# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN

def Simpson13(dIN):
	# Definir Dados
		# Precisão
	pDec = dIN.pDec
	mm.mp.dps = pDec
		# Tratamento das String de Função
	sf = tSf(dIN.sf)
	sdf = tSf(dIN.sdf)
		# Pontos de Análise
	a = mm.mpf(dIN.a)
	b = mm.mpf(dIN.b)
	h = mm.mpf((b-a)/2)
	xh = mm.mpf(a+h)
		# Funções dos pontos
	fa = f(a,sf,pDec)
	fxh = f(xh,sf,pDec)
	fb = f(b,sf,pDec)
	
	I = mm.mpf((h/3)*((fa)+(4*fxh)+(fb)))
	E = mm.mpf('0')
	# Executar Cálculo de Erro
	if(dIN.vsdf==1):
		c = mm.mpf('0')
		fdc = mm.mpf('0')
		# COM valor de C definido
		if(dIN.vc==1):
			c = mm.mpf(dIN.c)
		# SEM valor de C definido -> c = metade do intervalo
		else:
			c = xh
		fdc = f(c,sdf,pDec)
		
		E = mm.mpf((mm.power(h,5)/90)*fdc)

	# Gerar e Retornar Resposta
	resp = ""
	if(dIN.vsdf==1):
		resp += ("1/3 de Simpson\n\nI = "+str(I)+" ± "+str(E))
		resp += ("\n\nI+E = "+str(mm.mpf(I+E)))
		resp += ("\nI-E = "+str(mm.mpf(I-E)))
	else:
		resp += ("1/3 de Simpson\n\nI = "+str(I))
	return resp