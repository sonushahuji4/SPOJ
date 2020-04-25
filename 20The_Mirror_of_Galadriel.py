# Problem Statement Link : https://www.spoj.com/problems/AMR12D/

for _ in range(int(input())):
	st = list(input())
	n = len(st)
	ans = "YES"
	for i in range(n // 2):
		if st[i] != st[n - i-1]:
			ans = "NO"
			break
	print(ans)
