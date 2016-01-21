def find(l , s, start, end):

	if end - start == 0:
		if l[start] == s:
			return start
		else:
			return None

	mid = (start + end) / 2

	if l[mid] == s:
		return mid

	index = mid
	while l[index] == '' and index <= end:
		index += 1

	if l[index] == s:
		return index

	if l[index] == '':
		return find(l, s, start, mid-1)

	if l[index] > s: 
		return find(l, s, start, mid-1)
	else:
		return find(l, s, index+1, end)

	
if __name__ == '__main__':
	l = ['at' , '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
	print(find(l, 'ball', 0, len(l)-1))