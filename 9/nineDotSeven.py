def fill(screen, x, y, c):
	if x < 0 or x > len(screen)-1 or y < 0 or y > len(screen[0])-1:
		return

	if screen[x][y] == c:
		return

	screen[x][y] = c	

	fill(screen, x-1, y, c)
	fill(screen, x+1, y, c)
	fill(screen, x, y-1, c)
	fill(screen, x, y+1, c)

def printScreen(screen):
	for i in screen:
		line = []
		for j in i:
			line.append(str(j))
		l = ', '.join(line)
		print(l)



if __name__ == '__main__':
	screen = [
			 [0, 0, 0, 0, 0, 0],
			 [0, 1, 1, 1, 0, 0],
			 [0, 1, 1, 1, 0, 0],
			 [0, 1, 1, 1, 0, 0],
			 [0, 0, 0, 0, 0, 0]
			 ]
	printScreen(screen)
	fill(screen, 2, 2, 0)
	printScreen(screen)