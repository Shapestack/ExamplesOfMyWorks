from bs4 import BeautifulSoup as bs
import requests

print('1.Москва', '2. Санкт-Петербург', '3. Новосибирск')

name_city = input('Введите название города: ').lower()

if name_city == '1':
	name = 'Moscow'
	rus_name = 'Москве'
elif name_city == '2':
	name = 'saint-petersburg'
	rus_name = 'Санкт-Петербурге'
elif name_city == '3':
	name = 'novosibirsk'
	rus_name = 'Новосибирске'

	
url = f'https://yandex.ru/pogoda/{name}/details/10-day-weather?via=mf'
page = requests.get(url)
soup = bs(page.text, 'lxml')

list1= []
link = soup.find_all('span', 'temp__value')
for i in range(2, len(link), 3):
	list1.append(link[i].text)

print(f'\nСегодня днем в {rus_name}: {list1[1]}')
print()

list2 = []	
link=soup.find_all('div', 'weather-table__daypart')
for i in link:
	list2.append(i.text)

lst3 = []
new = soup.find_all('span', 'a11y-hidden')
for i in new:
	lst3.append(i.text)


for i in range(0, 13, 3):
	print(lst3[i])
print()
	
for i in range(17, 32, 3):
	print(lst3[i])
print()

for i in range(34, 49, 3):
	print(lst3[i])
print()

for i in range(51, 64, 3):
	print(lst3[i])
print()





