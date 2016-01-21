def sortAnagrams(l):
	dicMap = {}
	for s in l:
		key = ''.join(sorted(s))
		if key in dicMap:
			dicMap[key].append(s)
		else:
			dicMap[key] = [s]

	result = []
	for k in dicMap:
		result += dicMap[k]

	return result

if __name__ == '__main__':
	a = ['aba', 'cdd', 'aab', 'dcd', 'wer', 'aaa', 'rew', 'baa', 'rwe']
	l = sortAnagrams(a)
	print l