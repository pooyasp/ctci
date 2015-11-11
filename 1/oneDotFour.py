def replaceSpaceV1(str_in):
	return str_in.replace(' ', '%20')

def replaceSpaceV2(str_in):
	
	result = ''
	for c in str_in:
		if c == ' ':
			result += '%20'
		else:
			result += c

	return result

if __name__ == '__main__':
	str_in1 = 'qwer rtrt rrry'
	str_in2 = 'qweqwe  qweqwe  qweqwe 		wrwer'
	

	print(replaceSpaceV1(str_in1))
	print(replaceSpaceV1(str_in2))

	print(replaceSpaceV2(str_in1))
	print(replaceSpaceV2(str_in2))