def findMaxSequence(l):
	max_s = (len(l), len(l), float('-inf'))
	current_s = (len(l), len(l), float('-inf'))

	index = len(l)-1

	while index > -1:
		self_s = (index, index, l[index])
		current_s = (index, current_s[1], current_s[2]+l[index])

		if self_s[2] > current_s[2] and self_s[2] > max_s[2]:
			max_s = self_s
			current_s = self_s
		elif current_s[2] > self_s[2] and current_s[2] > max_s[2]:
			max_s = current_s
			
		index -= 1
	return max_s


if __name__ == '__main__':
	l = [2, -8, 3, -2, 4 ,-10]
	print findMaxSequence(l)