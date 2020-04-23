# Problem Statement Link : https://www.spoj.com/problems/FCTRL2/
for _ in range(int(input())):
	n = int(input())
	ans = 1
	while n > 0:
		ans = ans * n
		n -= 1
	print(ans)
