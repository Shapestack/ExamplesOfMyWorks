class Main:
	def __init__(self, proff, fname, lname, sex, age):
		self.proff = proff
		self.fname = fname
		self.lname = lname
		self.sex = sex
		self.age = age
	
	def bio(self):
		print('Profession:', x.proff, '\nName:', x.fname, x.lname, '\nSex:', x.sex, '\nAge:', x.age)


class Principal(Main):
	pass

x = Principal('Principal', 'Eleanor', 'Savage', 'Woman', 45)
x.bio()
print()


class Teachers(Main):
	def __init__(self, proff, fname, lname, sex, age, exp, sal=None):
		super().__init__(proff, fname, lname, sex, age)
		self.exp = exp
		self.sal = sal
	
	def expirience(self):
		if x.exp == 1:
			print('Expirience:', x.exp, 'year')
		else:
			print('Expirience:', x.exp, 'years')
	
	def salary(self):
		print('Salary:', x.sal, '$ per/month')

x = Teachers('Mathematic teacher', 'Jane', 'Smith', 'Woman', 32, 6, 6000)
x.bio(), x.expirience(), x.salary()
print()

x = Teachers('Physics teacher', 'Ronald', 'Turner', 'Man', 43, 1, 5500)
x.bio(), x.expirience(), x.salary()
print()

x = Teachers('Biology teacher', 'Elizabeth', 'Gray', 'Woman', 28, 4, 5800)
x.bio(), x.expirience(), x.salary()
print()


class OtrEmployees(Teachers):
	pass

x = OtrEmployees('Janitor', 'Sam', 'Nicholson', 'Man', 54, 12, 4500)
x.bio(), x.expirience(), x.salary()
print()

x = OtrEmployees('School team coach', 'Stan', 'Woodman', 'Man', 31, 3, 5000)
x.bio(), x.expirience(), x.salary()


		
		