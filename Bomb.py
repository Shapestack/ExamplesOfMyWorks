class Main(object):
	def main_frame(self):
		return NotImplementedError()
	
	def main_powder(self):
		return NotImplementedError()
	
	def main_timer(self):
		return NotImplementedError()
	
	def main_launch(self):
		return NotImplementedError()
	
	def main_detonation(self):
		return NotImplementedError()

class Bomb(object):
	def __init__(self, frame, powder, timer, launch, detonation):
		self._frame = frame
		self._powder = powder
		self._timer = 60
		self._launch = False
		self._detonation = False
			
	def __str__(self):
		import time
		lch = input('Введите "on" чтобы запустить отсчет бомбы или "off" чтобы выйти: ').lower()
		while True:
			if lch == 'on':
				self._launch = True
				time.sleep(0.2)
				self._timer -= 1
				print(self._timer)
				if self._timer == 0:
					detonation = 'on'
					self._detonation = True
					print('Ба-бах!')
					break
			elif lch == 'off':
				detonation = 'off'
				break
		return f'Детонация [{detonation}]'

class Frame(object):
	print('Корпус')

class Powder(object):
	print('Порох')

class Timer(object):
	print('Таймер')

class Launch(object):
	print('Запуск')

class Detonation(object):
	print('Детонация\n')
	
class MainBomb(Main):
	def main_frame(self):
		return Frame()
	
	def main_powder(self):
		return Powder()
	
	def main_timer(self):
		return Timer()
	
	def main_launch(self):
		return Launch()
	
	def main_detonation(self):
		return Detonation()
		
	def create_bomb(self):
		frame = self.main_frame()
		powder = self.main_powder()
		timer = self.main_timer()
		launch = self.main_launch()
		detonation = self.main_detonation()
		return Bomb(frame, powder, timer, launch, detonation)

main = MainBomb()
b = main.create_bomb()
print(b)



	

		

