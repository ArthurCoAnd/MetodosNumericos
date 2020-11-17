import mpmath as mm

def BriotRuffini(poli, prec, x0):
	mm.mp.dps = prec
	n = len(poli)
	q = [poli[n-1]]
	for i in range(n-2,-1,-1):
		q.insert(0,poli[i]+(q[0]*x0))

	return q[0]