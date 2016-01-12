def findMagicIndexV1(l, s, e):
	
	if s == e:
		if l[s] == s:
			return s
		else:
			return -1

	i = (s + e) / 2

	if l[i] == i:
		return i

	if i > l[i]:
		return findMagicIndexV1(l, i+1, e)
	else:
		return findMagicIndexV1(l, s, i-1)

def findMagicIndexV2(l, s, e):
	if e < s: 
		return -1

	if s == e:
		if l[s] == s:
			return s
		else:
			return -1

	i = (s + e) / 2

	if l[i] == i:
		return i

	left = findMagicIndexV2(l, s, min(i-1, l[i]))
	if left != -1:
		return left

	right = findMagicIndexV2(l, max(i+1, l[i]), e)
	return right

if __name__ == '__main__':
	l = [-1, 0, 1, 2, 4, 5]

	print(findMagicIndexV1(l, 0, len(l)-1))
	print(findMagicIndexV2(l, 0, len(l)-1))

