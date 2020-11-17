import mpmath as mm

def Newton(poli, prec, x0, e, k):
	mm.mp.dps = prec
	n = len(poli)
	x = x0
	chave = True
	i = 0
	while(i<k and chave):
		f = mm.mpf("0")
		df = mm.mpf("0")
		for p in range(n-1,-1,-1):
			f = f + ( poli[p]*(x**p) )
			if(p>0):
				df = df + ( poli[p]*p*(x**(p-1)) )
		xAux = x
		x = x - (f/df)
		if(abs(x-xAux)<e):
			chave = False
		i += 1

	return x