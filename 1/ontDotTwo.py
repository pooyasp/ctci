def reverseV1(str_in):
	if len(str_in) <= 1:
		return str_in
	return str_in[-1] + reverseV1(str_in[:-1])

def reverseV2(str_in):
	result = ''
	for c in str_in:
		result = c + result
	return result

if __name__ == '__main__':
	str_in1 = 'pooya'
	str_in2 = ''
	str_in3 = 'a'

	print(reverseV1(str_in1))
	print(reverseV1(str_in2))
	print(reverseV1(str_in3))

	print(reverseV2(str_in1))
	print(reverseV2(str_in2))
	print(reverseV2(str_in3))