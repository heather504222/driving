age = input('請輸入年齡:')
age = int(age)
country = input('請輸入國家:')
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
elif country == '美國':
	if age >=16:
		print('你可以考駕照')
	else:
		print('你不可以考駕照')
else:
	print('國家只限於台灣及美國')