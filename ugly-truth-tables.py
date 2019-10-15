# (P ↔ Q) ⊕ R ≡ (P ↔ R) ⊕ Q

def xor(p, q):
	return p ^ q

def implies(p, q):
	return not p or q

def iff(p, q):
	return p == q

def pq(f):
	print('p\tq')
	for p in range(0, 2):
		for q in range(0, 2):
			print('%d\t%d\t%d' % (p, q, f(p, q)))

def pqr(f):
	print('p\tq\tr')
	for p in range(0, 2):
		for q in range(0, 2):
			for r in range(0, 2):
				print('%d\t%d\t%d\t%d' % (p, q, r, f(p, q, r)))

def pq_equiv(f, g):
	print('f:'); pq(f)
	print('g:'); pq(g)
	for p in range(0, 2):
		for q in range(0, 2):
			if f(p, q) != g(p, q):
				print('f !== g for case p=%d, q=%d' % (p, q))
				return False
	print('f === g :)')

def pqr_equiv(f, g):
	print('f:'); pqr(f)
	print('g:'); pqr(g)
	for p in range(0, 2):
		for q in range(0, 2):
			for r in range(0, 2):
				if f(p, q, r) != g(p,q,r):
					print('f !== g for case p=%d, q=%d, r=%d' % (p, q, r))
					return False
	print('f === g :)')

p = 0
q = 0
r = 0


#print('a')
# good
pqr_equiv(lambda p,q,r: xor(implies(p, q), r), lambda p,q,r: xor(implies(p, q), r))
# f !== g for case p=0, q=0
pq_equiv(lambda p,q: implies(p, not q), lambda p,q: implies(not p, q))
# f !== g for case p=0, q=0, r=0
pqr_equiv(lambda p,q,r: p and iff(q, r), lambda p,q,r: iff(p and q, p and r))
#good
pqr_equiv(lambda p,q,r: xor(iff(p, not q), r), lambda p,q,r: iff(p, not xor(q, r)))
#good
pq_equiv(lambda p,q: xor(p, not q), lambda p,q: xor(not p, q))
#good
pqr_equiv(lambda p,q,r: xor(iff(p, q), r), lambda p,q,r: iff(p, xor(q, r)))
#good
pq_equiv(lambda p,q: iff(p, not q), lambda p,q: iff(not p, q))
pqr_equiv(lambda a,b,c: implies(implies(a,b), c), lambda a,b,c: implies(a, implies(b, c)))


pqr_equiv(lambda a,b,c: a and (b or c), lambda a,b,c: (a and b) or (a and c))