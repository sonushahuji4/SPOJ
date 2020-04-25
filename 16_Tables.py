# Problem Statement Link : https://www.spoj.com/problems/AE1B/

n, k, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sum_ = k * s
count_ = 0
for data in arr[::-1]:
	if sum_ <= data:
		count_ += 1
		break
	sum_ = sum_ - data
	count_ += 1
print(count_)