# Problem Statement Link : https://www.spoj.com/problems/AMR10G/
# http://coderpoem.blogspot.com/2015/11/spoj-solution-amr10g-christmas-play.html

for _ in range(int(input())):
	n, k = map(int, input().split())
	arr = list(map(int, input().split()))
	arr.sort()
	min_ = arr[k-1] - arr[0]
	if k == 1:
		ans = min_
	else:
		for i in range(n-k):
			ans = arr[i+k] - arr[i+1]
			min_ = min(min_,ans)
		ans = min_
	print(ans)
