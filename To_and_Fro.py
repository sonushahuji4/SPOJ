# https://www.spoj.com/problems/TOANDFRO/
while True:
	n = int(input())
	if n == 0:
		break
	arr = list(input())
	arr_len = len(arr)
	for i in range(n, arr_len, n + n):
		temp = arr[i:n + i]
		temp.reverse()
		j = i
		for element in temp:
			arr[j] = element
			j += 1

	for i in range(n):
		for j in range(i, arr_len, n):
			print(arr[j], end="")
	print()
