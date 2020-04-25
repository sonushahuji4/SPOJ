# Problem Statement Link : https://www.spoj.com/problems/ALCATRAZ1/

for _ in range(int(input())):
	num = input()
	arr = list(num)
	sum_ = 0
	for i in arr:
		sum_ += int(i)
	print(sum_)
