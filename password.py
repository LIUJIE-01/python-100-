'''
password = input('请输入密码: ')
	while True:
	if password == 'a123456':
		print('登录成功')
		break
	else:
		print('登陆失败')
'''
password = 'a123456'
i = 3
while True:
	pwd = input('请输入密码: ')
	if pwd == password:
		print('登陆成功！')
		break
	else:
		i-=1
		print('密码错误！ 还有',i,'次数')
	if i == 0:
		break