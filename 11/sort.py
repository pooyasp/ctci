import random

def mergeSort(l, start, end):
	if end - start == 0:
		return

	mid = (start + end) / 2

	mergeSort(l, start, mid)
	mergeSort(l, mid+1, end)
	merge(l, start, mid, end)

def merge(l, start, mid, end):
	temp = []
	i1 = start
	i2 = mid+1
	
	while True:
		
		if l[i1] <= l [i2]:
			temp.append(l[i1])
			i1 += 1 
			if i1 == mid+1:
				break
		else:
			temp.append(l[i2])
			i2 += 1
			if i2 == end+1:
				break

	while i1 != mid+1:
		temp.append(l[i1])
		i1 += 1

	i = start
	for v in temp:
		l[i] = v
		i += 1  

def quickSort(l, start, end):
	if start < end:
		pivot = partition(l, start, end)
		quickSort(l, start, pivot - 1)
		quickSort(l, pivot + 1, end)

def partition(l, start, end):
	pivot = l[end]

	i = start

	for j in range(start, end):
		if l[j] < pivot:
			temp = l[i]
			l[i] = l[j]
			l[j] = temp
			i += 1

	temp = l[i]
	l[i] = l[end]
	l[end] = temp

	return i


if __name__ == '__main__':
	l = []
	for i in range(10):
		l.append(random.randint(1, 1000))

	print l
	#mergeSort(l, 0, len(l)-1)
	quickSort(l, 0, len(l)-1)	
	print l	
