# Problem Statement Link : https://www.spoj.com/problems/ADDREV/
def reverse(num):
	zeros = 10
	while num % 10 == 0:
		num = num // zeros
	rev = 0
	while num:
		last = num % 10
		rev = (rev * 10) + last
		num = num // 10
	return rev


for _ in range(int(input())):
	num1, num2 = map(int, input().split())
	num1 = reverse(num1)
	num2 = reverse(num2)
	sum_ = num1 + num2
	ans = reverse(sum_)
	print(ans)
