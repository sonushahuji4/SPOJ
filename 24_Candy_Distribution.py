# Problems Statement Link : https://www.spoj.com/problems/CADYDIST/

# Hint : Cost of highest type of candy assign to class which has smallest number of students

while True:
	n = int(input())
	if n == 0:
		break
	classType = list(map(int, input().split()))
	costOfCandy = list(map(int, input().split()))
	classType.sort()
	costOfCandy.sort()
	costOfCandy.reverse()
	ans = 0
	for i in range(n):
		ans += classType[i] * costOfCandy[i]
	print(ans)
