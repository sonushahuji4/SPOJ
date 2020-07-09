# Problem Statement Link : https://www.spoj.com/problems/FCTRL/

for _ in range(int(input())):
	n = int(input())
	ans = 0
	while n > 0:
		n = n // 5
		ans += n
	print(ans)

