# Problem Statement Link : https://www.spoj.com/problems/ALCATRAZ2/

# WA
arr = list(map(int, input().split()))
arr.insert(0,0)
li = [0 for i in range(len(arr))]
for _ in range(int(input())):
	a, b = map(int, input().split())
	if arr[a] <= arr[b]:
		small = a
	else:
		small = b
	if li[small] == 0:
		li[small] = 1
ans = 0
for i in range(1,len(li)):
	if li[i] == 0:
		ans += arr[i]
print(ans)

# 3 14 5 2 3 4 1 9
# 4
# 1 2
# 2 3
# 4 5
# 7 8