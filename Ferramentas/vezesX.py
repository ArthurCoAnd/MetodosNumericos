def vezesX(s):
	r = ""
	tam = len(s)
	p = 0
	while(p<tam):
		if(s[p]=="x" or s[p]=="X"):
			if(s[p-1]!="*" and s[p-1]!="(" and p>0):
				r += "*x"
			if(s[p+1]!="*" and s[p+1]!="," and s[p+1]!=")" and p<tam-1):
				r += "x*"
			else:
				r += s[p]
		else:
			r += s[p]
		p += 1
	return r