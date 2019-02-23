code = 'a123456'
i = 3
while i > 0:
	password = input('請輸入密碼:')
	if code == password:
		print('密碼正確')
		break
	else:
		i = i - 1
		if i > 0:
			print('密碼錯誤,還有', i, '次機會')
		else:
			print('沒有機會了')	
	print('登入失敗')
		