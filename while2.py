while True:
	mode = input('请输入游戏模式: ')
	if mode == 'q':
		break
	elif mode == '1':
		print('启动游戏模式一')
	elif mode == '2':
		print('启动游戏模式二')
	else:
		print("只能输入 1/2/q")