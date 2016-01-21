def toStrThreeDigit(n):
	dic = {90: 'ninty', 80: 'eighty', 70: 'seventy', 60: 'sixty', 
	       50: 'fifty', 40: 'fourty', 30: 'thirty', 20: 'twenty', 
		   19: 'ninteen', 18: 'eighteen', 17: 'seventeen', 16: 'sixteen',
		   15: 'fifteen', 14: 'fourteen', 13: 'thirteen', 12: 'twelve', 
		   11: 'eleven', 10: 'ten', 9: 'nine', 8: 'eight', 
		   7: 'seven', 6: 'six', 5: 'five', 4: 'four', 
		   3: 'three', 2: 'two', 1: 'one'}

	result = ''

	first = n / 100
	n = n % 100

	if first != 0:
		result = dic[first] + ' Hundred'

	if n != 0:
		if n in dic:
			return result + ' ' + dic[n]
		else:
			second = n / 10
			third = n % 10

			result = result + ' ' + dic[second*10] + ' ' + dic[third]

	return result

def toStr(n):
	if n == 0:
		return 'zero'

	suffix = ['', ' Thousand', ' Million', ' Billion']
	result = []
	index = 0
	
	while n > 0:
		result = [toStrThreeDigit(n % 1000) + suffix[index]] + result
		n /= 1000
		index += 1
	
	return ', '.join(result)

if __name__ == '__main__':
	print toStr(1234)