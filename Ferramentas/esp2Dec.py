'''
esp2Dec - Especiais para Decimal

Transforma strings de Funções Especiais para Decimal
	ex: "cos(X)" -> "de.Decimal(cos(x))"
'''

def esp2Dec(s):
	s = sin2dec(s)
	s = cos2dec(s)
	s = tan2dec(s)
	# s = e2Dec(s)
	s = x2Dec(s)
	
	return s

def x2Dec(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="x"):
			r += "de.Decimal(x)"
		else:
			r += s[p]
		p += 1
	return r

def e2Dec(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="e"):
			r += "de.Decimal(e)"
		else:
			r += s[p]
		p += 1
	return r

def cos2dec(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="c"):
			if(s[p+1]=="o"):
				if(s[p+2]=="s"):
					if(s[p+3]=="("):
						aux = 4
						strAux = ""
						while (s[p+aux] != ")"):
							strAux += s[p+aux]
							aux += 1
						r += "de.Decimal(math.cos("+strAux+"))"
						p += aux
					else:
						continue
				else:
					continue
			else:
				continue
		else:
			r += s[p]
		p += 1
	return r

def sin2dec(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="s"):
			if(s[p+1]=="i"):
				if(s[p+2]=="n"):
					if(s[p+3]=="("):
						aux = 4
						strAux = ""
						while (s[p+aux] != ")"):
							strAux += s[p+aux]
							aux += 1
						r += "de.Decimal(math.sin("+strAux+"))"
						p += aux
					else:
						continue
				else:
					continue
			else:
				continue
		else:
			r += s[p]
		p += 1
	return r

def tan2dec(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="t"):
			if(s[p+1]=="a"):
				if(s[p+2]=="n"):
					if(s[p+3]=="("):
						aux = 4
						strAux = ""
						while (s[p+aux] != ")"):
							strAux += s[p+aux]
							aux += 1
						r += "de.Decimal(math.tan("+strAux+"))"
						p += aux
					else:
						continue
				else:
					continue
			else:
				continue
		else:
			r += s[p]
		p += 1
	return r

#'acos', 'asin', 'atan', 'atan2', 'ceil', 'cos', 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor', 'fmod', 'frexp', 'hypot', 'ldexp', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh'