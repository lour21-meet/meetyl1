class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def fav_breakfast(self,food):
		print(self.name + ' loves eating' + food + ' for breakfast!')
	def fav_s(self,sport):
		print(self.name + ' loves' + sport)

person1 = Person("Albert",16,"Jerusalem",'Male')
person1.fav_breakfast(' lasagna')
person1.fav_s(' swimming')

class Song(object):
	def __init__(self,song):
		self.song = song
	def sing_me_a_song(self):
		for x in song:
			print(x)

flower_song = Song(['Roses are red', 'Violets are blue',])