# Give TLE
def isPrime(n):
	if n == 1:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True


for _ in range(int(input())):
	start_, end_ = map(int, input().split())
	for i in range(start_, end_ + 1):
		if isPrime(i) == True:
			print(i)

# SAME LOGIC GETS ACCESPTED IN CPP
# # include <iostream>
# # include <cmath>
# # include <vector>
# # include <algorithm>
#
# using namespace std;
# bool isPrime(int n)
# {
# 	int j;
# 	if (n == 1)
# 	{
# 		return false;
# 	}
# 	for (j=2; j * j <= n; j++)
# 	{
# 		if (n % j == 0)
# 			return false;
# 	}
# 	return true;
#
# }
# int main()
# {
# 	int t;
# 	cin >> t;
# 	while (t - -)
# 		{
# 			int start_, end_, i;
# 			cin >> start_;
# 			cin >> end_;
# 			for (i=start_; i <= end_; i++)
# 			{
# 				if (isPrime(i) == true)
# 				{
# 				cout << i << "\n";
# 				}
# 			}
# 		}
# 	return 0;
# }
