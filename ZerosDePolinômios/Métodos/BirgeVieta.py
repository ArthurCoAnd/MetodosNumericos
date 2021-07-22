from numpy import zeros
from Ferramentas.f import f
from Ferramentas.erro import erro

def BirgeVieta(p,d,k=1):
	gp = len(p)
	x = d["x0"]
	fx = f(x,d["sf"])
	er = fx
	resultados = [[k,x,fx,er]]
	while(True):
		k += 1
		b = zeros(gp)
		for i in range(gp-1,-1,-1):
			if i == gp-1:
				b[i] = p[i]
			else:
				b[i] = p[i] + b[i+1]*x
		c = zeros(gp)
		for i in range(gp-1,0,-1):
			if i == gp-1:
				c[i] = b[i]
			else:
				c[i] = b[i] + c[i+1]*x
		xm = x - (b[0]/c[1])
		fx = f(xm,d["sf"])
		er = erro(x,xm,fx)
		x = xm
		resultados.append([k,xm,fx,er])
		if er < d["e"] or k > d["km"]:
			break
	return k-1, x, fx, er, resultados