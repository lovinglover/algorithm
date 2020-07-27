# Author:Jack

class Dog():
	def __init__(self, name):
		self.type = "dog"
		self.count = 0
		self.name = name

	def order(self, count):
		self.count = count

class Cat():
	def __init__(self, name):
		self.type = "cat"
		self.count = 0
		self.name = name

	def order(self, count):
		self.count = count

class Animal():
	def __init__(self):
		self.dog = []
		self.cat = []
		self.count = 0

	def add(self, obj):
		obj.order(self.count)
		if obj.type == "dog":
			self.dog.append(obj)
		else:
			self.cat.append(obj)
		self.count += 1

	def pullAll(self):
		while self.dog and self.cat:
			if self.dog[0].count > self.cat[0].count:
				print(self.cat.pop(0).name, end=" ")
			else:
				print(self.dog.pop(0).name, end=" ")

		while self.dog:
			print(self.dog.pop(0).name, end=" ")

		while self.cat:
			print(self.cat.pop(0).name, end=" ")
		print("")

	def pullDog(self):
		while self.dog:
			print(self.dog.pop(0).name, end=" ")
		print("")

	def pullCat(self):
		while self.cat:
			print(self.cat.pop(0).name, end=" ")
		print("")

	def isEmpty(self):
		return True if not self.cat and not self.dog else False

	def isDogEmpty(self):
		return not self.dog

	def isCatEmpty(self):
		return not self.cat


if __name__ == '__main__':
	animal = Animal()
	dog1 = Dog("1")
	dog2 = Dog("2")
	dog3 = Dog("3")
	cat1 = Cat("4")
	cat2 = Cat("5")
	cat3 = Cat("6")
	animal.add(dog1)
	animal.add(cat1)
	animal.add(dog2)
	animal.add(cat2)
	animal.add(dog3)
	animal.add(cat3)
	# animal.pullAll()
	# animal.pullCat()
	animal.pullDog()