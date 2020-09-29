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
		# Pontos de Análise
	a = mm.mpf(dIN.a)
	b = mm.mpf(dIN.b)
	h = mm.mpf((b-a)/3)
	xh1 = mm.mpf(a+h)
	xh2 = mm.mpf(b-h)
		# Funções dos pontos
	fa = f(a,sf,pDec)
	fxh1 = f(xh1,sf,pDec)
	fxh2 = f(xh2,sf,pDec)
	fb = f(b,sf,pDec)
	
	I = mm.mpf(((3*h)/8)*((fa)+(3*fxh1)+(3*fxh2)+(fb)))
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
		
		E = mm.mpf((3/80)*mm.power(h,5)*fdc)
		I = mm.mpf(I-E)

	# Retornar Resposta
	return I