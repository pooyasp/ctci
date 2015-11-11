def insert(n, m , i, j):
	m_p = m << i

	mask = (~((0 - 1) << (j - i + 1))) << i

	n_p = n & ~mask

	return n_p | m_p

if __name__ == '__main__':
	n = int('10000000000', 2)
	m = int('10011', 2)
	r = insert(n, m, 2, 6)
	print(bin(r))