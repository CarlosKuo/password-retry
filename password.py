# 密碼重試程式

# 先在程式碼中 設定好密碼 password = 'a123456'
# 讓使用者 [最多輸入 3 次密碼]
# 不對的話，就印出 "密碼錯誤! 還有 __ 次機會"
# 對的話，就印出 "登入成功!"

# password = 'a123456'
# i = 3 # 剩餘機會
# while True:
# 	pwd = input('請輸入密碼: ')
# 	if pwd == password:
# 		print('登入成功')
# 		break # 逃出迴圈
# 	else:
# 		i = i - 1
# 		print('密碼錯誤!還有', i, '次機會')
# 		if i == 0:
# 			break


# 不寫 True 的條件式
password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('請輸入密碼: ')
	if pwd == password:
		print('登入成功')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有', i, '次機會')
		else:
			print('沒機會嘗試了!要鎖帳號了啦!')

