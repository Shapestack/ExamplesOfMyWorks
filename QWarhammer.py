import random

class Warhammer:	
	def __init__(self):
		self.health = 1000
		self.max_health =1000
		self.dead = 0
astartes_health = Warhammer()

class Progenoid:
	def __init__(self):
		self.have = 2
		self.addition_heal = 200
		self.use = 1
		self.not_left = 0
astartes_progenoid = Progenoid()

class Ammo:
	def __init__(self):
		self.bolt = 30
		self.shot_bolt = 1
		self.no_ammo = 0
		self.frag_grenade = 1
		self.minigun = 1000
astartes_ammo = Ammo()

class Enemy_names:
	def __init__(self, name):
		self.name = name	
heretic_name = Enemy_names('Heretic')
chaos_marine_name = Enemy_names('Chaos marine')		

print('Welcome to battle simulation of the Ultramar!\n')
interface=['- - - - - - - - - - - - - - - - - - -',  #0
'-------------------', #1
'_ _ _ _________________________ _ _ _', #2
'______________________________________'] #3	

class Encounters:	
	War=True
	while War:
		class Enemy_health:
			def __init__(self, health, health_head, health_torso, dead):
				self.health = health
				self.health_head = health_head
				self.health_torso = health_torso
				self.dead = dead
				
		heretic_hp = Enemy_health(100, 2, 80, 0)
		chaos_marine_hp = Enemy_health(300, 100, 200, 0)
		
		print('\nYou on the battlefield. Where you going?\n')
		print('\nCheck the system: i - invetory\n')
		way=input('1. |Direct| \n// Go: ').lower()
		print()
		
		#inventory
		if way in ('i', 'inventory'):
			inventory_while = True
			while inventory_while:
				inventory = [str(astartes_health.health)+' HP', str(astartes_ammo.bolt)+' Bolt', str(astartes_progenoid.have)+' Progenoid']
				print(inventory)
				print('Use: 1. Progenoid 2. Exit\n')
				inventory_choice = input(f'// Choice: ').lower()
				print()
				
				if inventory_choice in ('1', 'progenoid'):
					if astartes_progenoid.have > astartes_progenoid.not_left:
						if astartes_health.health < astartes_health.max_health:
							astartes_progenoid.have = astartes_progenoid.have - astartes_progenoid.use
							astartes_health.health=astartes_health.health + astartes_progenoid.addition_heal
							if astartes_health.health>=astartes_health.max_health:
								astartes_health.health=astartes_health.max_health
						elif astartes_health.health>=astartes_health.max_health:
							print('To much health.\n')
							pass
					elif astartes_progenoid.have<=astartes_progenoid.not_left:
						astartes_progenoid.have==astartes_progenoid.not_left
						print('No have progenoid\'s.\n')
						pass
				elif inventory_choice in ('2', 'exit'):
					break		
				else:
					print('Wrong data\n')
					continue
					
		#ways		
		elif way in ('1','direct'):
			random_encounter = random.randrange(1, 2)
			if random_encounter == 1:
				print(f'You meet {heretic_name.name} and fight will begin!')
				turn = 0
				NEXT_TURN = 1			
				battle = True
				while battle:		
					turn = turn+NEXT_TURN
									
					class Enemies_damage:
						def __init__(self, attack):
							self.attack = attack		
							
					heretic = Enemies_damage(random.randrange(5, 20))
					chaos_marine = Enemies_damage(random.randrange(25, 45))
					
					class Weapon_damage:
						def __init__(self, attack):
							self.attack=attack
							
					bolter=Weapon_damage(random.randrange(30, 50))
					chainsword=Weapon_damage(random.randrange(25, 35))
					fists=Weapon_damage(random.randrange(20, 30))
					
					#critical hits
					CRIT=2
					crit_chance=random.randrange(1, 5)
						
					print(f'{interface[2]}\n')
					print('What you will do?: \n')
					
					hrt=input('Attack with: 1. |Bolter| 2. |Chaisword| 3. |Fist|\n//: ').lower()
					
					print(f'\n{interface[3]}\n')
					print(f'\n             {turn} TURN.\n')
					if hrt in ('1', 'bolter'):
						if astartes_ammo.bolt>astartes_ammo.no_ammo:
							astartes_ammo.bolt=astartes_ammo.bolt - astartes_ammo.shot_bolt
							astartes_ammo.bolt==astartes_ammo.no_ammo
							bolter_random_damage=random.randrange(1, 4)	
							if bolter_random_damage==1:
								if crit_chance==1:
									CRIT*=bolter.attack
									heretic_hp.health=heretic_hp.health - CRIT
									print(f'You inflicted "{bolter.attack} dmg" in head with bolter!\nHIS HEAD BLOW UP!\nCrit 2x! {CRIT} dmg.')
								else:
									heretic_hp.health=heretic_hp.health - bolter.attack
									print(f'You inflicted "{bolter.attack} dmg" in head with bolter!')									
							elif bolter_random_damage==2:
								if crit_chance==1:
									CRIT*=bolter.attack
									heretic_hp.health=heretic_hp.health - CRIT
									print(f'You inflicted "{bolter.attack} dmg" with bolter! It\'s look very painfully!\nCrit 2x! {CRIT} dmg.')
								else:
									heretic_hp.health=heretic_hp.health - bolter.attack
									print(f'You inflicted "{bolter.attack} dmg" with bolter! It\'s look very painfully!')
							elif bolter_random_damage==3:
								if crit_chance==1:
									CRIT*=bolter.attack
									heretic_hp.health=heretic_hp.health - CRIT
									print(f'You inflicted "{bolter.attack} dmg" with bolter! Goodlike!\nCrit 2x! {CRIT} dmg.')
								else:
									heretic_hp.health=heretic_hp.health - bolter.attack
									print(f'You inflicted "{bolter.attack} dmg" with bolter! Goodlike!')
						if astartes_ammo.bolt<=astartes_ammo.no_ammo:					
							astartes_ammo.bolt=astartes_ammo.no_ammo
							print('- -/\\No ammo/\\- -\nYou pass the turn!')
							pass
							
					elif hrt in ('2', 'chainsword'):
						heretic_hp.health=heretic_hp.health - chainsword.attack
						chainsword_random_damage=random.randrange(1, 4)
						if chainsword_random_damage==1:
							print(f'You inflicted "{chainsword.attack} dmg" with chainsword! And cruelly saw his torso')
						elif chainsword_random_damage==2:
							print(f'You inflicted "{chainsword.attack} dmg" with chainsword! And ripped his torso on the pieces!')
						elif chainsword_random_damage==3:
							print(f'You inflicted "{chainsword.attack} dmg" with chainsword! His torso will be destroyed!')
							
					elif hrt in ('3', 'fist'):
						heretic_hp.health=heretic_hp.health - fists.attack
						punch=random.randrange(1, 4)
						if punch==1:
							print(f'You inflicted "{fists.attack} dmg" with fist! And punching Heretic in the face!')
						elif punch==2:
							print(f'You inflicted "{fists.attack} dmg" with fist! And smash his head!')
						elif punch==3:
							print(f'You inflicted "{fists.attack} dmg" with fist! Blood sprayed from his nose!')
					else:
						print('You pass the turn')			
													
					if heretic_hp.health<=heretic_hp.dead:
						print(f'\n-Xx|{heretic_name.name} dead!|xX-')
						print(f'{interface[1]}\n')
						break	
					astartes_health.health=astartes_health.health - heretic.attack
					
					if astartes_health.health<=astartes_health.dead:
						print('////You dead////')
						quit()
						
					print(f'\n({heretic_name.name} {heretic_hp.health} hp left)')
					print(f'{interface[0]}\n')
					print('\n—*{'+str(heretic_name.name), 'attack!}*—')
					print('-x{'+str(heretic_name.name)+ ' inflicted '+str(heretic.attack)+'"dmg"!}x-','\n'*2)
					print(f'{interface[0]}\n')
					print(f'[// You |{astartes_health.health}| HP left //]')
					print(f'[|| {astartes_ammo.bolt} ammo in the bolter left ||]')
									
			elif random_encounter==2:
				print('Hello')
				
		else:
			print('\nNOT PASS')	