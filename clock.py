import time

class Clock_start:
	def __init__(self, sec, min, hour, day):
		self.sec = sec
		self.min = min
		self.hour = hour
		self.day = day
		
clock_start = Clock_start(0, 0, 0, 0)
clock_end = Clock_start(61, 61, 25, 32)

while True:
	run = input('Press "X" to Run or "Y" to Exit: ').lower()
	if run == 'x':
		pass
	elif run == 'y':
		break
	while True:
		time.sleep(1)
		if clock_start.sec <= clock_end.sec:
			clock_start.sec += 1		
			if clock_start.sec == clock_end.sec:
				clock_start.sec = 0
				clock_start.min += 1			
			elif clock_start.min == clock_end.min:
				clock_start.min = 0
				clock_start.hour += 1 			
			elif clock_start.hour == clock_end.hour:
				clock_start.hour = 0
				clock_start.day += 1			
			elif clock_start.day == clock_end.day:
				clock_start.day = 0
				
		
		print(f'{clock_start.day}:{clock_start.hour}:{clock_start.min}:{clock_start.sec}', end='\r')
	

		
		
		
	