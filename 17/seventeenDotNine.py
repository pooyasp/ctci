def creatMap(book):
	dic = {}
	for w in book:
		word = wo.lower().strip()
		if word in dic:
			dic[word] += 1
		else:
			dic[word] = 1

	return dic

def findFrequency(word, dic):
	if dic == None or word == None:
		return None

	if word in dic:
		return dic[word]
	else:
		return 0
