import math
import numpy as np
# Importando Ferramentas
from Ferramentas.título import título
from ZeroDeFunções.dadosZDF import dados
# Importando Funções
from ZeroDeFunções.Funções.f import f
# Import Métodos
from ZeroDeFunções.Métodos.PontoFixo import pontoFixo
from ZeroDeFunções.Métodos.NewtonRaphson import newtonRaphson
from ZeroDeFunções.Métodos.Secante import secante

def validarIntervalo(d):
	título("Validar Intervalo", '=')
	resp = ""

	# Verificar se o intervalo é crescete
	resp += "Intervalo Crescente (a>b)\t-\t"
	# Intervalos Crescentes
	if(d.a<d.b):
		resp += "Válido\n"
		resp += continuidade(d)
		resp += xRaizesInter(d)
		# Intervalos com apenas* 1 Raiz
		if(FuncTS(d)):
			# Intervalos que funções derivada primeira não alteram sinal
			if(dFuncTS(d)):
				resp += "Bissecção\t\t\t-\tIntervalo Válido\n"
				resp += "Posição Falsa\t\t\t-\tIntervalo Válido\n"
			else:
				resp += "Bissecção\t\t\t-\tIntervalo Inválido\n"
				resp += "Posição Falsa\t\t\t-\tIntervalo Inválido\n"
		else:
			resp += "Bissecção\t\t\t-\tIntervalo Inválido\n"
			resp += "Posição Falsa\t\t\t-\tIntervalo Inválido\n"
	# Intervalos NÃO Crescentes
	else:
		resp += "Inválido\n"
		resp += "Bissecção\t\t\t-\tIntervalo Inválido\n"
		resp += "Posição Falsa\t\t\t-\tIntervalo Inválido\n"

	chave = True
	try:
		pontoFixo(d)
	except:
		chave = False
	if(chave):
		resp += "Ponto Fixo\t\t\t-\tIntervalo Válido\n"
	else:
		resp += "Ponto Fixo\t\t\t-\tIntervalo Inválido\n"

	# Intervalos que funções derivada segunda não alteram sinal
	if (ddFuncTS(d)):
		chave = True
		try:
			newtonRaphson(d)
		except:
			chave = False
		if(chave):
			resp += "Newton-Raphson\t\t\t-\tIntervalo Válido\n"
		else:
			resp += "Newton-Raphson\t\t\t-\tIntervalo Inválido\n"

	chave = True
	try:
		pontoFixo(d)
	except:
		chave = False
	if(chave):
		resp += "Secante\t\t\t\t-\tIntervalo Válido"
	else:
		resp += "Secante\t\t\t\t-\tIntervalo Inválido"


	return resp

# Verificar Continuidade das Funções
def continuidade(d):
	r = ""
	# Continuidade Função f(x)
	chave = True
	for x in np.arange(d.a,d.b,d.e):
		try:
			f(x,d.sf)
		except:
			chave = False
	r += "Continuidade em f(x)\t\t-\t"
	if(chave):
		r += "Válida\n"
	else:
		r += "Inválida\n"

	# Continuidade da Derivada Primeira da Função f(x)
	chave = True
	for x in np.arange(d.a,d.b,d.e):
		try:
			f(x,d.sdf)
		except:
			chave = False
	r += "Continuidade em f'(x)\t\t-\t"
	if(chave):
		r += "Válida\n"
	else:
		r += "Inválida\n"

	# Continuidade da Derivada Segunda da Função f(x)
	chave = True
	for x in np.arange(d.a,d.b,d.e):
		try:
			f(x,d.sddf)
		except:
			chave = False
	r += "Continuidade em f''(x)\t\t-\t"
	if(chave):
		r += "Válida\n"
	else:
		r += "Inválida\n"

	return r

# Verificar Quantas Raizes Pode Ter no Intervalo
def xRaizesInter(d):
	raizes = 0
	r = ""
	for x in np.arange(d.a,d.b,d.e):
		try:
			if(f(x,d.sf)*f(x-d.e,d.sf)<0):
				raizes += 1
		except:
			r += "Possíveis raízes no Intervalo\t-\tIntervalo Inválido\n"
			return r
	r += "Possíveis raízes no Intervalo\t-\t%i\n"%(raizes)
	return r

# Verificar se a Função Troca de Sinal Apenas Uma Vez
def FuncTS(d):
	raizes = 0
	chave = True
	for x in np.arange(d.a,d.b,d.e):
		try:
			if(f(x,d.sf)*f(x-d.e,d.sf)<0):
				raizes += 1
		except:
			chave = False
			break
	if(raizes!=1):
		chave = False
	return chave

# Verificar se a Função Derivada Primeira Troca de Sinal
def dFuncTS(d):
	chave = True
	for x in np.arange(d.a,d.b,d.e):
		try:
			if(f(x,d.sdf)*f(x-d.e,d.sdf)<0):
				chave = False
				break
		except:
			chave = False
			break
	return chave
	
# Verificar se a Função Derivada Segunda Troca de Sinal
def ddFuncTS(d):
	chave = True
	for x in np.arange(d.a,d.b,d.e):
		try:
			if(f(x,d.sddf)*f(x-d.e,d.sddf)<0):
				chave = False
				break
		except:
			chave = False
			break
	return chave