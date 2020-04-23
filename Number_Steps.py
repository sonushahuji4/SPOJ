# Problem Statement Link : https://www.spoj.com/problems/NSTEPS/
for _ in range(int(input())):
	x, y = map(int, input().split())
	if x == y or x - y == 2:
		if x & 1 == 0:
			print(x + y)
		else:
			print((x + y) - 1)
	else:
		print("No Number")
