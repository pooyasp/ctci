def findKthV1(k):
	i = 1
 	c = 1

	while True:
		
		if i == k:
			return c

		c += 2

		r = c

		while r % 7 == 0:
			r /= 7
		while r % 5 == 0:
			r /= 5
		while r % 3 == 0:
			r /= 3

		if r == 1:
			i += 1


def findKthV2(k):
	l = [1]

	q3 = [1]
	q5 = [1]
	q7 = [1]

	for i in range(k-1):
		

		n3 = q3[0] * 3
		while n3 in l:
			q3.pop(0)
			n3 = q3[0] * 3
	
		n5 = q5[0] * 5
		while n5 in l:
			q5.pop(0)
			n5 = q5[0] * 5
	
		n7 = q7[0] * 7
		while n7 in l:
			q7.pop(0)
			n7 = q7[0] * 7
	
		n = 0

#		print(l)
#		print(q3)
#		print(q5)
#		print(q7)
#		print(n3)
#		print(n5)
#		print(n7)
#		print('------')

		if n3 <= n5 and n3 <= n7:
			n = n3
			q3.pop(0)

		if n5 < n3 and n5 <= n7:
			n = n5
			q5.pop(0)

		if n7 < n3 and n7 < n5:
			n = n7
			q7.pop(0)

		l.append(n)

		q3.append(n)
		q5.append(n)
		q7.append(n)

	return l[-1]




if __name__ == '__main__':

#	print(findKthV1(150))
	print(findKthV2(15000))