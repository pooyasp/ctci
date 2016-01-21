def encode(xml, dic):
	l =  [e.strip() for e in xml.split('<') if e != '']

	result = []
	for e in l:
		if e[0] == '/' and e[-1] == '>':
			result.append('0')
			continue

		for ep in e.replace('>' , ' 0 ').split(' '):
			if '=' not in ep:
				if ep in dic:
					result.append(str(dic[ep]))
				else:
					result.append(ep)
			else:
				tv = ep.split('=')
				result.append(str(dic[tv[0]]))
				result.append(tv[1][1:-1])
			print result
	
	print result
	return ' '.join(result)



if __name__ == '__main__':
	dic = {'family' : 1, 'person' : 2, 'firstName' : 3, 'lastName' : 4, 'state' : 5}

	xml =  '<family lastName="McDowell" state="CA">' + '\n'
	xml += '	<person firstName="Gayle">Some Message</person>' + '\n'
	xml += '</family>'

	print encode(xml, dic)