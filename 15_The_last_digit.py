# Problem Statement Link : https://www.spoj.com/problems/LASTDIG/

for _ in range(int(input())):
	a, b = map(int, input().split())
	ans = 0
	if a == 0 and b > 0:
		print(ans)
	elif a > 0 and b == 0:
		print(1)
	else:
		if b % 4 == 0:
			rem = 4
		else:
			rem = b % 4
		ans = pow(a, rem, 1000000007)
		print(ans % 10)
