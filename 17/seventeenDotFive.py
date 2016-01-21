def countHits(pattern, guess):
	hit = 0

	pattern_dic = {}
	guess_dic = {}

	for i in range(len(pattern)):
		if pattern[i] == guess[i]:
			hit += 1
		else:
			if pattern[i] in pattern_dic:
				pattern_dic[pattern[i]] += 1
			else:
				pattern_dic[pattern[i]] = 1
				
			if guess[i] in guess_dic:
				guess_dic[guess[i]] += 1
			else:
				guess_dic[guess[i]] = 1

	pseudo_hit = 0
	for k in guess_dic:
		if k in pattern_dic:
			pseudo_hit += min(pattern_dic[k], guess_dic[k])

	return hit, pseudo_hit

if __name__ == '__main__':
	print countHits('RGBY', 'GGRR')