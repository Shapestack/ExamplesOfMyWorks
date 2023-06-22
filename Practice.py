
#простейшие арифметические операции
'''
arith=input('Введите оператор: ')

def arithmetic(a, b, c=arith):
	if c=='-':
		print(a-b)
	elif c=='+':
		print(a+b)
	elif c=='*':
		print(a*b)
	elif c=='/':
		print(a/b)
	else:
		print('Неизвестная операция')
arithmetic(3, 2)
'''

'''
#Високосный год

year_leap=int(input('Введите год: '))

def is_year_leap(year=year_leap):
	for i in range(1764, 2133, 4):
		if i==year:
			print(year, True, '- Високосный')
			break
	if i!=year:
		print(year, False, '- Не високосный')
is_year_leap()
'''

'''
sqr=float(input('Введите сторону квадрата: '))

def square(side=sqr):
	diagonal=2**0.5*side
	area=diagonal**2/2
	perimetr=side*4
	print((f'{diagonal} Диагональ квадрата,\n{area} Площадь квадрата,\n{perimetr} Периметр квадрата.'))
square()
'''

'''
#Времена года

day=int(input('Введите день месяца: '))

def season(number_month=day):
	for i in range(1,13):
		if number_month in (3, 4, 5):
			print('Весна')
			if number_month==3:
				print('Март')
			elif number_month==4:
				print('Апрель')
			elif number_month==5:
				print('Май')
			break
		if number_month in (6, 7, 8):
			print('Лето')
			if number_month==6:
				print('Июнь')
			elif number_month==7:
				print('Июль')
			elif number_month==8:
				print('Август')
			break
		if number_month in (9, 10, 11):
			print('Осень')
			if number_month==9:
				print('Сентябрь')
			elif number_month==10:
				print('Октябрь')
			elif number_month==11:
				print('Ноябрь')
			break
		if number_month in (12, 1, 2):
			print('Зима')
			if number_month==12:
				print('Декабрь')
			elif number_month==1:
				print('Январь')
			elif number_month==2:
				print('Февраль')
			break
		else:
			print('Неверный день месяца')
			break

season()
'''
	
'''
#Простое число
while True:
	number_prime=int(input('Введите проверочное число: '))
	n=0
	for i in range(2, number_prime//2+1):
		if number_prime%i==0:
				n=n+1
	if n<=0:
		print('Простое число -', True)	
	else:
		print('Составное число -', False)
'''			




				
		




