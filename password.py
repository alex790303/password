code = 'a123456'
i = 3
while True:
	password = input('請輸入密碼:')
	if code == password:
		print('密碼正確')
		break
	elif code != password:
		i = i - 1
		if i >= 0:
			print('密碼錯誤，還有', i, '次機會')
		else:
			print('登入失敗')
			break
		