# Problem Statement Link : https://www.spoj.com/problems/BWIDOW/

for _ in range(int(input())):
	max_1 = max_2 = 0
	for i in range(int(input())):
		r, R = map(int, input().split())
		if r > max_1:
			max_1 = r
			index_ = i
		elif R > max_2:
			max_2 = R
	if max_1 > max_2:
		print(index_ + 1)
	else:
		print(-1)
