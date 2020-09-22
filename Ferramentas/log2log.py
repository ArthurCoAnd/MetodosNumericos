'''
log2log - log base e para log base 10

Transforma strings de "log" em log 10
	ex: "log(x)" -> "log(x,10)"

Transforma strings "ln" em log e
	ex: "ln(x)" -> "log(x)"
'''
def log2log(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="l"):
			if(s[p+1]=="o"):
				if(s[p+2]=="g"):
					if(s[p+3]=="("):
						'''
						aux = 4
						strAux = ""
						while (s[p+aux] != ")"):
							strAux += s[p+aux]
							aux += 1
						r += "log("+strAux+",10)"
						p += aux
						'''
						r += "log10("
						p += 3
					else:
						continue
				else:
					continue
			'''	
			elif(s[p+1]=="n"):
				if(s[p+2]=="("):
					aux = 3
					strAux = ""
					while (s[p+aux] != ")"):
						strAux += s[p+aux]
						aux += 1
					r += "log("+strAux+")"
					p += aux
				else:
					continue
			
			else:
				continue
			'''
		else:
			r += s[p]
		p += 1
	return r