# Problem Statement Link : https://www.spoj.com/problems/GLJIVE/

ans = 0
status = False
for _ in range(10):
	num = int(input())
	ans += num
	if ans >= 100:
		if ans <= 100 + num / 2:
			status = True
		else:
			status = True
			ans = ans - num
	if status == True:
		break
print(ans)
