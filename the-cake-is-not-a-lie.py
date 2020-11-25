def solution2(seq):	
	seq = seq.replace(" ", "")
	t = ''
	for c in seq:
		if seq.count(t+c) <= 1:
			break
		elif len(t) * seq.count(t) == len(seq):
			return seq.count(t)
		else:
		 t += c
	if len(t) * seq.count(t) == len(seq):
		return seq.count(t)
	return 0
