def rand7():
	while True:
		n = rand5() * 5 + rand5()
		if n < 21:
			return n % 7