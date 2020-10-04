# Importar Bibliotecas
import mpmath as mm
# Importar Ferramentas
from Ferramentas.f import f
from Ferramentas.tratamentoSf import tratamentoSf as tSf
	# Ferramentas Integração Numérica
from IntegraçãoNumérica.FerramentasIN.DadosIN import DadosIN as dIN
from IntegraçãoNumérica.FerramentasIN.RespostaIN import RespostaIN as rIN

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
		# Quantidade e Tamanho dos Intervalos
	m = int(dIN.m)
	if(dIN.ve==1):
		c = (a+b)/2
		if(dIN.vc==1):
			c = dIN.c
		m = mDe(a,b,c,dIN.e,sdf,pDec)
	h = mm.mpf((b-a)/(3*m))
	bi = mm.mpf(a+(3*h))

		# Chave Para Somar Erro ao Longo das Interações
	chave = False
	if(dIN.vsdf==1 and dIN.vc==0):
		chave = True

	r = método(I,E,a,bi,sf,sdf,m,1,h,chave,pDec)

		# Calular Erro com c definido pelo usuário
	if(dIN.vsdf==1 and dIN.vc==1):
		c = mm.mpf(dIN.c)
		fdc = f(c,sdf,pDec)
		r.E = mm.mpf((m/80)*mm.power(h,5)*fdc)

	# Gerar e Retornar Resposta
	resp = ""
	if(dIN.vsdf==1):
		resp += ("3/8 de Simpson Repetido\n\nI = "+str(r.I)+" ± "+str(r.E))
		resp += ("\n\nI+E = "+str(mm.mpf(r.I+r.E)))
		resp += ("\nI-E = "+str(mm.mpf(r.I-r.E)))
	else:
		resp += ("3/8 de Simpson Repetido\n\nI = "+str(r.I))
	return resp

def método(I,E,a,b,sf,sdf,m,mk,h,chave,pDec):
	mm.mp.dps = pDec
	resp = rIN(I,E)
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

	resp.I = mm.mpf(resp.I+(((3*h)/8)*((fa)+(3*fxh1)+(3*fxh2)+(fb))))
	resp.E = mm.mpf(resp.E+((3/80)*mm.power(h,5)*fdc))

	if(mk<m):
		a = b
		b = mm.mpf(b+(3*h))
		mk += 1
		resp = método(resp.I,resp.E,a,b,sf,sdf,m,mk,h,chave,pDec)

	return resp

# Calcular quantidade de intervalos m para garantir um erro menor que e
def mDe(a,b,c,e,sdf,pDec):
	mm.mp.dps = pDec
	# h = (b-a)/(3*m) => m = (b-a)/(3*h)
	# e > -m(h^5/80)fdc => e > -(b-a)(h^4/240)fdc => h < sqrt(sqrt( 240*e / (b-a)fdc ))
	# m > (b-a)/sqrt(sqrt( 240*e / (b-a)fdc ))
	a = mm.mpf(a)
	b = mm.mpf(b)
	c = mm.mpf(c)
	e = mm.mpf(e)
	fdc = mm.mpf(f(c,sdf,pDec))
	difBA = mm.mpf(b-a)

	m = mt.ceil(abs(difBA/mm.sqrt(mm.sqrt((240*e)/(difBA*fdc)))))

	return m