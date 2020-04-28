# Porblem Statement Link : https://www.spoj.com/problems/FACEFRND/

friends_of_friends_list = set()
n = int(input())
for _ in range(n):
	li = list(map(int, input().split()))
	id = li[0]
	friends_of_friends_list.add(id)
	bobs_friend_having_number_of_friends = li[1]
	del li[0]
	del li[0]
	for i in range(bobs_friend_having_number_of_friends):
		friends_of_friends_list.add(li[i])
print(len(friends_of_friends_list)-n)
