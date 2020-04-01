import random
k = input('请输入开始值: ')
j = input('请输入结束值: ')
k = int(k)
j = int(j)
r = random.randint(k,j)
count = 0
while True:
	count += 1
	num = input('猜猜数字: ')
	num = int(num)
	if num == r:
		print('你猜中了！')
		break
	elif num < r:
		print('比答案小') 
	elif num > r:
		print('比答案大')
	print('这是你猜的第', count, '次')