def isUniqueCharV1(str_in):
	hash_map = {}
	for c in str_in:
		if c in hash_map:
			return False
		else:
			hash_map[c] = True
	return True

def isUniqueCharV2(str_in):
	for i in range(len(str_in)):
		if str_in[i] in str_in[i+1:]:
			return False
	return True


if __name__ == '__main__':
	strIn1 = "qwertyuiopasdfghjklzxcvbnm{}><"
	print(isUniqueCharV1(strIn1))
	print(isUniqueCharV2(strIn1))
	strIn2 = "qwertyuiopasdfghjk{lzxcvbnm{}><"
	print(isUniqueCharV1(strIn2))
	print(isUniqueCharV2(strIn2))
	strIn3 = "qwertyuiopasdfghjklzxcvbnm{}><"
	print(isUniqueCharV1(strIn3))
	print(isUniqueCharV2(strIn3))