#Банковский вклад
while True:
	percent = float(input('Введите процентную ставку: %'))	
	dep = float(input('Введите размер вашего депозита: '))	
	year = int(input('Введите число лет для вклада: '))		
	
	def bank(deposit=dep, years=year):
		sum = percent*deposit/100*years
		deposit += sum			
		if years%10 in range(2, 5):
			print(f'|{deposit} Ваш общий счет.\n|{sum} Процент от годовых за {years} года.')	
		elif years%10 == 1:
			print(f'|{deposit} Ваш общий счет.\n|{sum} Процент от годовых за {years} год.')
		else:
			print(f'|{deposit} Ваш общий счет.\n|{sum} Процент от годовых за {years} лет.')			
	
	bank()