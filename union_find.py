uf = {}

def union(a, b):
	uf[find(a)] = find(b)

def find(a):
	uf.setdefault(a, a)
	if uf[a] != a:
		uf[a] = find(uf[a])
	return uf[a]