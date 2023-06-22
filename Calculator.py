
while True:
	try:
		choice = int(input('Выберите тип операций: "1" - если стандартная, "2" - если процентная, "3" - извлечение корня.\n//: '))
		
		if choice == 1:
			print('\nСтандартная\n')		
			while True:
				print('+ сложение, - вычитание, * умножение, ** возведение в степень, \n'
				'/ деление, // деление без остатка, % деление с выводом остатка, \n')
				fir_vl = float(input('Введите первое значение: '))
				opr = input('Введите арифметический оператор: ')
				sec_vl = float(input('Введите второе значение: '))
					
				class Calculator:
					def __init__(self, first_value, operator, second_value):
						self.fr = first_value
						self.op = operator
						self.sc = second_value
							
				cal = Calculator(fir_vl, opr, sec_vl)	
					
					
				if cal.op == '+':
					print(cal.fr+cal.sc)
				elif cal.op == '-':
					print(cal.fr-cal.sc)
				elif cal.op == '*':
					print(cal.fr*cal.sc)
				elif cal.op == '**':
					print(cal.fr**cal.sc)
				elif cal.op == '/':
					print(cal.fr/cal.sc)
				elif cal.op == '//':
					print(cal.fr//cal.sc)
				elif cal.op == '%':
					print(cal.fr%cal.sc)
				print()
					
				exit=input('Нажмите "Y" чтобы выйти в меню, нажмите "Num" чтобы продолжить: ').lower()
				if exit == 'y':
					break
				else:
					pass
					
		elif choice == 2:
			print('\nПроцентная\n')
			while True:
				print('%n найти процент от числа, %= процент от двух чисел (процентное отношение), \n'
				'%+ прибавить процент к числу, %- отнять процент от числа, \n'
				'%< на сколько первое число меньше второго 100% - найти 100 процентов.\n')
				fir_vl = float(input('Введите первое значение: '))
				opr = input('Введите оператор: ')
				sec_vl = float(input('Введите второе значение: '))
				
				class Calculator:
					def __init__(self, first_value, operator, second_value):
						self.fr = first_value
						self.op = operator
						self.sc = second_value
							
				cal = Calculator(fir_vl, opr, sec_vl)
				
				
				if cal.op == '%n':
					print(cal.fr*cal.sc/100)
				elif cal.op == '%=':
					print(cal.fr/cal.sc*100)
				elif cal.op == '%+':
					print(cal.sc*(1+cal.fr/100))
				elif cal.op == '%-':
					print(cal.sc*(1-cal.fr/100))
				elif cal.op == '%<':
					print(100-cal.fr/cal.sc*100)
				print()
				
				exit=input('Нажмите "Y" чтобы выйти в меню, нажмите "Num" чтобы продолжить: ').lower()
				if exit == 'y':
					break
				else:
					pass
					
		elif choice == 3:
			print('\nИзвлечение корня\n')
			while True:
				fir_vl = float(input('Введите число для извлечения корня: '))
				opr = input('Введите оператор √: ')

		
				class Calculator:
					def __init__(self, first_value, operator):
						self.fr = first_value
						self.op = operator
							
				cal = Calculator(fir_vl, opr)
								
				if cal.op == '√':
					print(cal.fr**0.5)
				else:
					pass
				print()
					
				exit=input('Нажмите "Y" чтобы выйти в меню, нажмите "Num" чтобы продолжить: ').lower()
				if exit == 'y':
					break
				else:
					pass
					
	except:
		continue
				