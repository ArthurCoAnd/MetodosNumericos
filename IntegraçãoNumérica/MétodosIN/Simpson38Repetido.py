# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN

def Simpson38Repetido(dIN):
	# Definir Dados
		# Precisão
	pDec = dIN.pDec
	mm.mp.dps = pDec
		# Tratamento das Strings de Funções
	sf = tSf(dIN.sf)
	sdf = tSf(dIN.sdf)
		# Resultados
	I = mm.mpf('0')
	E = mm.mpf('0')
		# Pontos de Análise
	a = mm.mpf(dIN.a)
	b = mm.mpf(dIN.b)
	m = int(dIN.m)
	h = mm.mpf((b-a)/(3*m))
	bi = mm.mpf(a+(3*h))

		# Chave Para Somar Erro ao Longo das Interações
	chave = False
	if(dIN.vsdf==1 and dIN.vc==0):
		chave = True

	I = método(I,E,a,bi,sf,sdf,m,1,h,chave,pDec)

		# Calular Erro com c definido pelo usuário
	if(dIN.vsdf==1 and dIN.vc==1):
		c = mm.mpf(dIN.c)
		fdc = f(c,sdf,pDec)
		E = mm.mpf((m/80)*mm.power(h,5)*fdc)
		I = mm.mpf(I-E)

	return I

def método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec):
	mm.mp.dps = pDec
	xh1 = mm.mpf(a+h)
	xh2 = mm.mpf(b-h)
	fa = f(a,sf,pDec)
	fb = f(b,sf,pDec)
	fxh1 = f(xh1,sf,pDec)
	fxh2 = f(xh2,sf,pDec)
	fdc = mm.mpf('0')
	# Cálculo do erro SEM valor de c definido pelo usuário -> c = metade do intervalo
	if(chave):
		c = mm.mpf((a+b)/2)
		fdc = f(c,sdf,pDec)

	I = mm.mpf(I+(((3*h)/8)*((fa)+(3*fxh1)+(3*fxh2)+(fb))))
	E = mm.mpf(E+((3/80)*mm.power(h,5)*fdc))

	if(mk<m):
		a = b
		b = mm.mpf(b+(3*h))
		mk += 1
		I = método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec)
	
	I = mm.mpf(I-E)
	
	return I