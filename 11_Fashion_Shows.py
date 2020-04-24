# Problem Statement Link : https://www.spoj.com/problems/FASHION/

for _ in range(int(input())):
	n = int(input())
	men = list(map(int, input().split()))
	women = list(map(int, input().split()))
	men.sort()
	women.sort()
	n = n - 1
	ans = 0
	while n > -1:
		ans += men[n] * women[n]
		n -= 1
	print(ans)
