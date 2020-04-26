# Problem Statement Link : https://www.spoj.com/problems/BISHOPS/

# Hint : Look for pattern

while True:
	try:
		n = int(input())
		if n == 1:
			ans = 1
		else:
			ans = n + (n - 2)
		print(ans)
	except:
		break
