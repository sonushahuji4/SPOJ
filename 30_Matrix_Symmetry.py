# Problem Statement Link : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/matrix-symmetry/

for _ in range(int(input())):
	n = int(input())
	matrix = []
	for _ in range(n):
		li = list(input())
		matrix += [li]
	vertical = [1] * (n // 2)
	horizontal = [1] * (n // 2)
	for i in range(n // 2):
		for j in range(n // 2):
			# horizontal
			if matrix[i][j] != matrix[n - 1 - i][j]:
				horizontal[i] = 0
			# Vertical
			if matrix[i][j] != matrix[i][n - 1 - j]:
				vertical[j] = 0
	row = horizontal.count(1)
	col = vertical.count(1)
	if row == n // 2 and col == n // 2:
		print("BOTH")
	elif row == 0 and col != 0:
		print("VERTICAL")
	elif col == 0 and row != 0:
		print("HORIZONTAL")
	else:
		print("NO")
