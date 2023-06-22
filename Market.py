#Market
class Market(object):
	def fruits(self):
		return 'Нет товара'
		return NotImplementedError
	
	def vegetables(self):
		return 'Нет товара'
		return NotImplementedError
	
	def furnitures(self):
		return 'Нет товара'
		return NotImplementedError
	
	def electronics(self):
		return 'Нет товара'
		return NotImplementedError
		
class Fruits(object):
	def __init__(self, name):
		self._name=name
	
	def __str__(self):
		return self._name

class Vegetables(object):
	def __init__(self, name):
		self._name=name
	
	def __str__(self):
		return self._name

class Furniture(object):
	def __init__(self, name):
		self._name=name
	
	def __str__(self):
		return self._name

class Electronics(object):
	def __init__(self, name):
		self._name=name
	
	def __str__(self):
		return self._name

class Magnit(Market):
	def fruits(self):
		fru=['Apples', 'Bananas', 'Oranges', 'Watermelons', 'Avocados']
		return fru
	
	def vegetables(self):
		veg=['Potatos', 'Carrots', 'Onions', 'Cabbages', 'Piccles']
		return veg
	
	def furnitures(self):
		fur=['Chairs', 'Beds']
		return fur
	
	def electronics(self):
		elec=['TV', 'Fridges', 'Computers']
		return elec
		
class Ikea(Market):
	def furnitures(self):
		fur=['Tables', 'Chairs', 'Beds', 'Closets', 'Dressers']
		return fur
	
	def electronics(self):
		elec=['TV', 'Fridges', 'Computers', 'Microwaves', 'Washers']
		return elec
	
def get_market(id):
	if id == 'magnit':
		return Magnit()
	elif id == 'ikea':
		return Ikea()
	else:
		return 'Error'

print('Magnit, Ikea\n')
mar=get_market(input('Введите магазин: ').lower())
print(
'Fruits -', mar.fruits(), 
'\nVegetables -', mar.vegetables(),
'\nFurnitures -', mar.furnitures(),
'\nElectronics - ', mar.electronics()
)

		