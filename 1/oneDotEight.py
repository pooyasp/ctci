def isRotation(s1, s2):
	if len(s1) != len(s2) or s1 == '':
		return False

	s1s1 = s1 + s1

	return s1s1.find(s2) > -1


if __name__ == '__main__':
	s1 = "waterbottle"
	s2 = "erbottlewat"

	print(isRotation(s1, s2))