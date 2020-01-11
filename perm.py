# returns all possible arrangements of the characters in s
def perm(s):
	print('called perm with ' + s)
	if len(s) <= 1:
		return [s]
	a = s[0]
	z = perm(s[1:])
	ans = []
	# insert a in every possible place in z
	for i in range(0, len(s)):
		for string in z:
			ans.append(string[:i] + a + string[i:])
	return ans
	
print(perm('012'))