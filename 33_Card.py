# Problem Statement Link : https://www.spoj.com/problems/CRDS/

# Approach one (wrong approach)
# prefix = []
# n = 1000000
# ans = 0
# for i in range(n + 1):
# 	ans += i * 2
# 	prefix += [ans]
# for _ in range(int(input())):
# 	n = int(input())
# 	print(prefix[n] + (n * (n - 1) // 2))

# Approach Two (Correct)
for _ in range(int(input())):
	n = int(input())
	print((2 * (n * (n + 1) // 2) + (n * (n - 1) // 2)) % 1000007)
