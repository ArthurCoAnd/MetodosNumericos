# Importar Bibliotecas
from math import *

def f(x,s):
	s = virgula2ponto(s)
	s = circunflexo2pow(s)
	s = sen2sin(s)
	s = log2log10(s)
	s = ln2log(s)
	s = vezesX(s)
	y = eval(s)
	return y

def virgula2ponto(s):
	return s.replace(",",".")

def sen2sin(s):
	return s.replace("sen","sin")

def circunflexo2pow(s):
	return s.replace("^","**")

def log2log10(s):
	return s.replace("log","log10")

def ln2log(s):
	return s.replace("ln","log")

def vezesX(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="x" or s[p]=="X"):
			chave = True
			# Verificar se ANTES do X pede Multiplicação
			if(s[p-1]!="*" and s[p-1]!="(" and s[p-1]!="^" and s[p-1]!="+" and s[p-1]!="-" and s[p-1]!="/" and p>0):
				r += "*x"
				chave = False
			# Verificar se DEPOIS do X pede Multiplicação
			if(p+1<tam):
				if(s[p+1]!="*" and s[p+1]!="," and s[p+1]!=")" and s[p+1]!="^" and s[p+1]!="+" and s[p+1]!="-" and s[p+1]!="/"):
					r += "x*"
					chave = False
			if(chave):
				r += s[p]
		else:
			r += s[p]
		p += 1
	return r