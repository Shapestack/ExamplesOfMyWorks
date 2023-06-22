
discount = float(input('Введите число: '))

lst=[]

def generate_sale_size(x=discount):
	print(x, 'Аргумент')
	for i in range(-75, 95, 5):
		if x >= i:
			if x >= 0:
				lst.append(f'+{i}-{i+5}%')
			elif x < 0:
				lst.append(f'{i}-({i+5})%')
		elif x < -75:
			lst.append('-75')

generate_sale_size()
print(lst[-1:][0])
