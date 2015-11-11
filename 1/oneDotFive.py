def compress(str_in):
	if str_in == '':
		return ''

	current_char = str_in[0]
	char_count = 0
	result = []

	for c in str_in:
		if current_char != c:
			result.append(current_char + str(char_count))
			current_char = c
			char_count = 1
		else:
			char_count +=1

	result.append(current_char + str(char_count))

	output = ''.join(result)

	if len(output) < len(str_in):
		return output
	else:
		return str_in


if __name__ == '__main__':

	str_in1 = 'aaabbbbbccc'
	str_in2 = 'abbbbbbcc'
	str_in3 = 'aabbcc'
	str_in4 = 'abcc'
	str_in5 = 'a'


	print(compress(str_in1))
	print(compress(str_in2))
	print(compress(str_in3))
	print(compress(str_in4))
	print(compress(str_in5))