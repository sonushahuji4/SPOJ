# Problem Statement Link : https://www.spoj.com/problems/SAMER08F/
while True:
	n = int(input())
	if n == 0:
		break
	ans = 0
	while n > 1:
		ans += n * n
		n -= 1
	print(ans + 1)
