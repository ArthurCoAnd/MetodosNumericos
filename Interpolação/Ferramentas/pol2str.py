def pol2str(pol):
	np = len(pol)
	s = f"{pol[np-1]:.7}*(x^{np-1})"
	for i in range(len(pol)-2,-1,-1):
		s += f" {pol[i]:+.7}*(x^{i})"
	return s