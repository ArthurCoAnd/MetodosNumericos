# Importar Bibliotecas
import math as mt
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN
from IntegraçãoNumérica.FerramentasIN.RespostaIN import RespostaIN as rIN

def TrapézioRepetido(dIN):
	# Definir Dados
		# Precisão
	pDec = dIN.pDec
	mm.mp.dps = pDec
		# Tratamento Strings de Funções
	sf = tSf(dIN.sf)
	sdf = tSf(dIN.sdf)
		# Respostas
	I = mm.mpf('0')
	E = mm.mpf('0')
		# Pontos de Análise
	a = mm.mpf(dIN.a)
	b = mm.mpf(dIN.b)
		# Quantidade e Tamanho dos Intervalos
	m = int(dIN.m)
	if(dIN.ve==1):
		c = (a+b)/2
		if(dIN.vc==1):
			c = dIN.c
		m = mDe(a,b,c,dIN.e,sdf,pDec)
	h = mm.mpf((b-a)/m)
	bi = mm.mpf(a+h)
		# Chave Para Somar Erro ao Longo das Interações
	chave = False
	if(dIN.vsdf==1 and dIN.vc==0):
		chave = True

	r = método(I,E,a,bi,sf,sdf,m,1,h,chave,pDec)

	if(dIN.vsdf==1 and dIN.vc==1):
		c = mm.mpf(dIN.c)
		fdc = f(c,sdf,pDec)
		r.E = mm.mpf(m*(mm.power(h,3)/12)*fdc)

	# Gerar e Retornar Resposta
	resp = ""
	if(dIN.vsdf==1):
		resp += ("Trapézio Repetido\n\nI = "+str(r.I)+" ± "+str(r.E))
		resp += ("\n\nI+E = "+str(mm.mpf(r.I+r.E)))
		resp += ("\nI-E = "+str(mm.mpf(r.I-r.E)))
	else:
		resp += ("Trapézio Repetido\n\nI = "+str(r.I))
	return resp

def método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec):
	mm.mp.dps = pDec
	resp = rIN(I,E)
		# Dados de Análise
	fa = f(a,sf,pDec)
	fb = f(b,sf,pDec)
	c = mm.mpf('0')
	# COM cálculo de erro a cada intervalo mas sem c definido -> c = metade do intervalo
	if(chave):
		c = mm.mpf((a+b)/2)
	fdc = f(c,sdf,pDec)

	resp.I = mm.mpf(resp.I+((h/2)*(fa+fb)))
	resp.E = mm.mpf(resp.E+((mm.power(h,3)/12)*fdc))

	if(mk<m):
		a = b
		b = mm.mpf(b+h)
		mk += 1
		resp = método(resp.I,resp.E,a,b,sf,sdf,m,mk,h,chave,pDec)
	
	return resp
	
# Calcular quantidade de intervalos m para garantir um erro menor que e
def mDe(a,b,c,e,sdf,pDec):
	mm.mp.dps = pDec
	# h = (b-a)/m => m = (b-a)/h
	# e > -m(h³/12)fdc => e > -(b-a)(h²/12)fdc => h < sqrt( 12*e / (b-a)fdc )
	# m > (b-a)/sqrt( 12*e / (b-a)fdc )
	a = mm.mpf(a)
	b = mm.mpf(b)
	c = mm.mpf(c)
	e = mm.mpf(e)
	fdc = mm.mpf(f(c,sdf,pDec))
	difBA = mm.mpf(b-a)

	m = mt.ceil(abs(difBA/mm.sqrt((12*e)/(difBA*fdc))))

	return m