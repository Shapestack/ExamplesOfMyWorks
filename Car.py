
#Car

class Main(object):
	def ignition(self):
		return NotImplementedError()
		
	def engine(self):
		return NotImplementedError()
	
	def tank(self):
		return NotImplementedError()
	
	def wheels(self):
		return NotImplementedError()

class Car(object):
	def __init__(self, ignition, engine, tank, wheels):
		self._ignition = False
		self._engine = False
		self._tank = 30 #топливо
		self._wheels = wheels
		
	def __str__(self):
		while True:
			ign = input('Введите "on" чтобы повернуть ключ зажигания или нажмите "off" чтобы оставить: ').lower()
			if ign == 'on':
				self._ignition = True
				print(bool(self._ignition))
				if self._tank > 0:
					self._engine = True
					print('Машина работает')
				else:
					print('Машина не заводится. Мало топлива.')
			elif ign == 'off':
				self._ignition = False
				print('Машина выключена.')
				quit()
			else:
				print('Неверная команда')

class Ignition(object):
	print('Ключ зажигания')

class Engine(object):
	print('Двигатель')

class Tank(object):
	print('Топливный бак')

class Wheels(object):
	print('Колеса')

class MainCar(Main):
	def main_ignition(self):
		return Ignition()
	
	def main_engine(self):
		return Engine()
	
	def main_tank(self):
		return Tank()
	
	def main_wheels(self):
		return Wheels()
	
	def create_car(self):
		ignition = self.main_ignition()
		engine = self.main_engine()
		tank = self.main_tank()
		wheels = self.main_wheels()
		return Car(ignition, engine, tank, wheels)

main = MainCar()
c = main.create_car()
print(c)


				
				
			