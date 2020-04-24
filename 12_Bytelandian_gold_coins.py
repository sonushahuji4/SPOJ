# Study Material 1 : https://www.youtube.com/watch?v=LvoLkONR5Bg
#                2 : https://www.youtube.com/watch?v=5dRGRueKU3M
# Problem Statement Link : https://www.spoj.com/problems/COINS/

# Solution :

dp = {}
dp[0] = 0
dp[1] = 1


def ans(n):
	if n in dp:
		return dp[n]
	else:
		dp[n] = max(n, ans(n // 2) + ans(n // 3) + ans(n // 4))
		return dp[n]


while True:
	try:
		n = int(input())
		print(ans(n))
	except:
		break
