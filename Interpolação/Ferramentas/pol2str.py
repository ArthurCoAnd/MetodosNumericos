def pol2str(pol):
	np = len(pol)
	s = f"{pol[np-1]}*(x^{np-1})"
	for i in range(len(pol)-2,-1,-1):
		s += f" {pol[i]:+}*(x^{i})"
	return s