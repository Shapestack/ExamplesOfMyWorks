import time
import random
from string import ascii_lowercase

coded=[input('Enter password: ').lower()]
decoded=[]

start=time.perf_counter()

p='Please wait.'
wh=True
while True:
	dec_str=random.choice(ascii_lowercase)
	dec_int=str(random.randrange(0, 10))	
	for i in dec_str:
		if dec_str in coded[0]:
			decoded.append(dec_str)
		else:
			pass
			
	for i in dec_int:			
		if dec_int in coded[0]:
			decoded.append(dec_int)
		else:
			pass
	
	union_dec=[''.join(decoded)]
	if union_dec==coded:
		break
	elif len(decoded)>=len(coded[0]):
		print(f'{union_dec}', end='\r')
		decoded.clear()		
	else:
		pass	
			
if union_dec==coded:
	print(coded, 'coded')
	print('Success')
	print(union_dec, 'decoded\n')
else:
	print('Not decoded')

end=time.perf_counter()
print(end-start, 'operation time left')