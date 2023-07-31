import random
start = int(input('輸入隨機數字範圍的起始值: '))
end = int(input('輸入隨機數字範圍的終點值: '))
r = random.randint(start, end)
count = 0

while True:
	count += 1
	num = int(input('輸入您要猜的數字: '))
	if r == num:
		print('你猜對了，答案是:', num, '\n你共猜了:', count, '次')
		break
	elif r > num:
		print('再大一點，你猜的數字比答案小')
	elif r < num:
		print('再小一點，你猜的數字比答案大')
	print('你共猜了', count, '次')


