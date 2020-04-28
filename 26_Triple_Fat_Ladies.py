# Problem Statement Link : https://www.spoj.com/problems/EIGHTS/
# Hint 1: Try to find out patterns in numbers
# Hint 2: Arithmetic progression
# Hint 3: Try to find about a = ? and d = ? in AP and then your are good to go.
# Spoiler : ans = a+(n-1)*d

for _ in range(int(input())):
	n = int(input())
	ans = 192 + (n - 1) * 250
	print(ans)
