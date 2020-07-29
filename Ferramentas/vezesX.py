'''
vezesX - Vezes X

Tenta adicionar o Char '*' antes e depois de x
	ex: "4x(5/7)" -> "4*x*(5/7)"
'''
def vezesX(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="x" or s[p]=="X"):
			chave = True
			if(s[p-1]!="*" and s[p-1]!="(" and p>0):
				r += "*x"
				chave = False
			if(p+1<tam):
				if(s[p+1]!="*" and s[p+1]!="," and s[p+1]!=")"):
					r += "x*"
					chave = False
			if(chave):
				r += s[p]
		else:
			r += s[p]
		p += 1
	return r