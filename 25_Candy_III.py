# Problem Statement Link : https://www.spoj.com/problems/CANDY3/

# Run Time Error
for _ in range(int(input())):
	n = int(input())
	sum_ = 0
	ans = "NO"
	for i in range(n):
		candy = int(input())
		sum_ = (sum_ + candy) % n
	if sum_ % n == 0:
		ans = "YES"
	print(ans)
