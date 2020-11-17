import mpmath as mm

def BirgeVieta(poli, prec, x0, e, k):
	mm.mp.dps = prec
	n = len(poli)
	x = x0
	chave = True
	i = 0
	while(i<k and chave):
		b = mm.mpf("0")
		c = mm.mpf("0")
		for p in range(n-1,-1,-1):
			b = poli[p] + (b*x)
			if(p>0):
				c = b + (c*x)
		xAux = x
		x = x - (b/c)
		if(abs(xAux-x)<e):
			chave = False
		i += 1

	return x