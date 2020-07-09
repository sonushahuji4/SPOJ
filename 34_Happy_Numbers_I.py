# Problem Statement Link : https://www.spoj.com/problems/HPYNOS/

# Solution :
n = int(input())
val = set()
ans = 0
while True:
	sum_of_square_of_n = 0
	while n:
		sum_of_square_of_n += (n % 10) * (n % 10)
		n = n // 10
	ans += 1
	if sum_of_square_of_n == 1:
		print(ans)
		break
	if sum_of_square_of_n in val:
		print(-1)
		break
	val.add(sum_of_square_of_n)
	n = sum_of_square_of_n
