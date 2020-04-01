country = input('请问你是哪国人: ')
age = input('你输入你的年龄: ')
age = int(age)
if country == '中国':
	if age >= 18:
		print('你可以考驾照了')
	else:
		print('还不可以哟')