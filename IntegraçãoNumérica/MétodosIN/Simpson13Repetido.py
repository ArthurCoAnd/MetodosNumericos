# Importar Bibliotecas
import mpmath as mm
import numpy as np
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN

def Simpson13Repetido(dIN):
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
	h = mm.mpf((b-a)/(2*m))
	bi = mm.mpf(a+(2*h))

		# Chave Para Somar Erro ao Longo das Interações
	chave = False
	if(dIN.vsdf==1 and dIN.vc==0):
		chave = True

	I = método(I,E,a,bi,sf,sdf,m,1,h,chave,pDec)

		# Calular Erro com c definido pelo usuário
	if(dIN.vsdf==1 and dIN.vc==1):
		c = mm.mpf(dIN.c)
		fdc = f(c,sdf,pDec)
		E = mm.mpf((m/2)*(mm.power(h,5)/90)*fdc)
		I = mm.mpf(I-E)

	return I

def método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec):
	mm.mp.dps = pDec
	fa = f(a,sf,pDec)
	fb = f(b,sf,pDec)
	xh = mm.mpf((a+b)/2)
	fxh = f(xh,sf,pDec)
	fdc = mm.mpf('0')
	if(chave):
		c = mm.mpf((a+b)/2)
		fdc = f(c,sdf,pDec)

	I = mm.mpf(I+((h/3)*((fa)+(4*fxh)+(fb))))
	E = mm.mpf(E+((mm.power(h,5)/90)*fdc))

	if(mk<m):
		a = b
		b = mm.mpf(b+(2*h))
		mk += 1
		I = método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec)
	
	I = mm.mpf(I-E)
	
	return I