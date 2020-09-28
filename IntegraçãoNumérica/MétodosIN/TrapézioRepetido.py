# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN
#from IntegraçãoNumérica.FerramentasIN.RespostaIN import RespostaIN as rIN

def TrapézioRepetido(dIN):
	# Definir Dados
		# Precisão
	pDec = dIN.pDec
	mm.mp.dps = pDec
		# 
	I = mm.mpf('0')
	E = mm.mpf('0')
	a = mm.mpf(dIN.a)
	b = mm.mpf(dIN.b)
	m = int(dIN.m)
	h = mm.mpf((b-a)/m)
	bi = mm.mpf(a+h)
	sf = tSf(dIN.sf)
	sdf = tSf(dIN.sdf)
		# Chave Para Somar Erro ao Longo das Interações
	chave = False
	if(dIN.vsdf==1 and dIN.vc==0):
		chave = True

	I = método(I,E,a,bi,sf,sdf,m,1,h,chave,pDec)

	if(dIN.vsdf==1 and dIN.vc==1):
		c = mm.mpf(dIN.c)
		fdc = f(c,sdf,pDec)
		E = mm.mpf((mm.power(h,3)/12)*fdc)
		I = mm.mpf(I-E)

	return I

def método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec):
	mm.mp.dps = pDec
	fa = f(b,sf,pDec)
	fb = f(b,sf,pDec)
	c = mm.mpf('0')
	fdc = mm.mpf('0')
	if(chave):
		c = mm.mpf((a+b)/2)
		fdc = f(c,sdf,pDec)

	I = mm.mpf(I+((h/2)*(fa+fb)))
	E = mm.mpf(E+((mm.power(h,3)/12)*fdc))

	if(mk<m):
		a = b
		b = mm.mpf(b+h)
		mk += 1
		I = método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec)
	
	I = mm.mpf(I-E)
	
	return I