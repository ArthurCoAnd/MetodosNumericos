# Importar Bibliotecas
import math as mt
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN
from IntegraçãoNumérica.FerramentasIN.RespostaIN import RespostaIN as rIN

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
		# Quantidade e Tamanho dos Intervalos
	m = int(dIN.m)
	if(dIN.ve==1):
		c = (a+b)/2
		if(dIN.vc==1):
			c = dIN.c
		m = mDe(a,b,c,dIN.e,sdf,pDec)
	h = mm.mpf((b-a)/(2*m))
	bi = mm.mpf(a+(2*h))

		# Chave Para Somar Erro ao Longo das Interações
	chave = False
	if(dIN.vsdf==1 and dIN.vc==0):
		chave = True

	r = método(I,E,a,bi,sf,sdf,m,1,h,chave,pDec)

		# Calular Erro com c definido pelo usuário
	if(dIN.vsdf==1 and dIN.vc==1):
		c = mm.mpf(dIN.c)
		fdc = f(c,sdf,pDec)
		r.E = mm.mpf((m/2)*(mm.power(h,5)/90)*fdc)

	# Gerar e Retornar Resposta
	resp = ""
	if(dIN.vsdf==1):
		resp += ("1/3 de Simpson Repetido\n\nI = "+str(r.I)+" ± "+str(r.E))
		resp += ("\n\nI+E = "+str(mm.mpf(r.I+r.E)))
		resp += ("\nI-E = "+str(mm.mpf(r.I-r.E)))
	else:
		resp += ("1/3 de Simpson Repetido\n\nI = "+str(r.I))
	return resp

def método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec):
	mm.mp.dps = pDec
	resp = rIN(I,E)
	fa = f(a,sf,pDec)
	fb = f(b,sf,pDec)
	xh = mm.mpf((a+b)/2)
	fxh = f(xh,sf,pDec)
	fdc = mm.mpf('0')
	# Cálculo do erro SEM valor de c definido pelo usuário -> c = metade do intervalo
	if(chave):
		c = mm.mpf((a+b)/2)
		fdc = f(c,sdf,pDec)

	resp.I = mm.mpf(resp.I+((h/3)*((fa)+(4*fxh)+(fb))))
	resp.E = mm.mpf(resp.E+((mm.power(h,5)/90)*fdc))

	if(mk<m):
		a = b
		b = mm.mpf(b+(2*h))
		mk += 1
		resp = método(resp.I,resp.E,a,b,sf,sdf,m,mk,h,chave,pDec)

	return resp

# Calcular quantidade de intervalos m para garantir um erro menor que e
def mDe(a,b,c,e,sdf,pDec):
	mm.mp.dps = pDec
	# h = (b-a)/(2*m) => m = (b-a)/(2*h)
	# e > -m(h^5/180)fdc => e > -(b-a)(h^4/360)fdc => h < sqrt(sqrt( 360*e / (b-a)fdc ))
	# m > (b-a)/sqrt(sqrt( 360*e / (b-a)fdc ))
	a = mm.mpf(a)
	b = mm.mpf(b)
	c = mm.mpf(c)
	e = mm.mpf(e)
	fdc = mm.mpf(f(c,sdf,pDec))
	difBA = mm.mpf(b-a)

	m = mt.ceil(abs(difBA/mm.sqrt(mm.sqrt((360*e)/(difBA*fdc)))))

	return m
