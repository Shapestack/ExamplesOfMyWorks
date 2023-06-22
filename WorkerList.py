class Corporation:
	print('Welcome to Workers List!''\n''------------------------')
	print('Insert \'Exit\' if you want to cancel session.','\n'*3)
	managers=[]
	engineers=[]
	builders=[]
	
	Corp=True
	while Corp:
		print('|1. Managers, 2. Engineers, 3. Builders.|''\n')
		work=input('Please choose a number type of workers: ').lower()
		print('\n_ _ _ ____________________ _ _ _\n')
		if work=='1':
			print('\nManagers\n')
			print('\n''Supporting functions: /del, /clear, /ret \n')
			while work:
				mng=input('\nPlease insert names: ').title()
				managers.append(mng)
				if mng=='/Clear':	
					managers.clear()
				elif mng=='/Del':
					del managers[-2::]
				elif mng=='/Ret':
					del managers[-1::]
					break
				print(managers)
			
		elif work=='2':
			print('Engineers')
			print('\n''Supporting functions: /del, /clear, /ret. \n')
			while work:
				eng=input('\nPlease insert names: ').title()
				engineers.append(eng)
				if eng=='/Clear':
					engineers.clear()
				elif eng=='/Del':
					del engineers[-2::]
				elif eng=='/Ret':
					del engineers[-1::]
					break
				print(engineers)
				
		elif work=='3':
			print('Builders')
			print('\n''Supporting functions: /del, /clear, /ret. \n')
			while work:
				bld=input('\nPlease insert names: ').title()
				builders.append(bld)
				if bld=='/Clear':
					builders.clear()
				elif bld=='/Del':
					del builders[-2::]
				elif bld=='/Ret':
					del builders[-1::]
					break
				print(builders)
				
		elif work=='exit':
			work==True
			while work:
				next=input('You wanna exit? Y/N: ').lower()
				if next=='n':
					break
				elif next=='y':
					quit()
				else:			
					print('\n#Error, wrong key word! Try again.\n')
					continue
			else:
				print('\n#Error, wrong key word! Try again.\n')
									
		print('\n'
		'Managers:', managers,'\n'
		'Engineers:', engineers,'\n'
		'Builders:', builders,'\n'
		)
		
			
	