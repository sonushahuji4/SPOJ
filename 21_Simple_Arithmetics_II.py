# Problem Statement Link : https://www.spoj.com/problems/ARITH2/

# Run time error
for _ in range(int(input())):
	arr = list(map(str,input().split()))
	ans = arr[0]
	for i in range(1,len(arr)-1):
		if arr[i] == "=":
			break
		if arr[i] == "/" or arr[i] == "*" or arr[i] == "+" or arr[i] == "-":
			operator = arr[i]
		else:
			if operator == '/':
				ans = int(ans) // int(arr[i])
			elif operator == '*':
				ans = int(ans) * int(arr[i])
			elif operator == '+':
				ans = int(ans) + int(arr[i])
			elif operator == '-':
				ans = int(ans) - int(arr[i])
	print(ans)
