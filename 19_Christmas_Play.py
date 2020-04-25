# Problem Statement Link : https://www.spoj.com/problems/AMR10G/

# WA
for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr.sort()
	print(arr[n - 1] - arr[n - k])
