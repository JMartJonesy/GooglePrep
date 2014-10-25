#Basic Hasmap using python hash function, naive and does not implement
#chaining

class HashMap:
	def __init__(self, size = 10):
		self.hashMap = [None] * size
		self.values = 0

	def add(self, key, value):
		index = self.hashIt(key)
		if self.values > (len(self.hashMap) * .75):
			self.resize()
		self.hashMap[index] = (key,value)
		self.values += 1

	def hashIt(self, key):
		return hash(key) % len(self.hashMap)
	
	def resize(self):
		oldHashMap = self.hashMap
		self.hashMap = [None] * (len(oldHashMap) * 2)
		for val in oldHashMap:
			if val != None:
				key, value = val
				self.add(key, value)

	def get(self, key):
		if self.contains(key):
			return self.hashMap[self.hashIt(key)][1]
		else:
			return None

	def getKeySet(self):
		keyList = []
		for val in self.hashMap:
			if val != None:
				key, value = val
				keyList.append(key)
		return set(keyList)

	def remove(self, key):
		if self.contains(key):
			self.hashMap[self.hashIt(key)] = None
			self.values -= 1

	def contains(self, key):
		return self.hashMap[self.hashIt(key)] != None

if __name__ == "__main__":
	h = HashMap()
	h.add("boobs", 10)
	print(h.get("boobs"))
	print(h.contains("nips"))
	print(h.getKeySet())
