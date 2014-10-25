class Heap:
	def __init__(self, heap = [None, None, None]):
		self.heap = heap
		self.addIndex = 0
	
	def insert(self, value):
		self.heap[self.addIndex] = value
		if(self.addIndex > 0):
			valueIndex = self.addIndex
			while(True):
				parentIndex = 0
				
				if(valueIndex % 2 == 0):
					parentIndex = (valueIndex-2)//2
				else:
					parentIndex = (valueIndex-1)//2	
				
				if(parentIndex >= 0 and self.heap[parentIndex] > value):
					temp = self.heap[parentIndex]
					self.heap[parentIndex] = value
					self.heap[valueIndex] = temp	
					valueIndex = parentIndex

				else:
					break
	
		self.addIndex += 1
		if(self.addIndex > (len(self.heap) - 1)):
			for i in range(0, len(self.heap)):
				self.heap.append(None)
	
	def removeMin(self):
		if(self.heap[0] == None):
			return None

		value = self.heap[0]
		self.heap[0] = self.heap[self.addIndex - 1]
		self.heap[self.addIndex - 1] = None
		
		index = 0
		while(True):
			leftIndex = (2*index) + 1
			rightIndex = (2*index) + 2
			if(rightIndex < len(self.heap)):
				leftVal = self.heap[leftIndex]
				rightVal = self.heap[rightIndex]
				if(leftVal != None and rightVal != None):
					if(leftVal < rightVal and leftVal < self.heap[index]):
						temp = self.heap[index]
						self.heap[index] = leftVal
						self.heap[leftIndex] = temp
						index = leftIndex
					elif(rightVal < leftVal and rightVal < self.heap[index]):
						temp = self.heap[index]
						self.heap[index] = rightVal
						self.heap[rightIndex] = temp
						index = rightIndex
					else:
						break
				elif(leftVal != None and leftVal < self.heap[index]):			
					temp = self.heap[index]
					self.heap[index] = leftVal
					self.heap[leftIndex] = temp
					index = leftIndex
				elif(rightVal != None and rightVal < self.heap[index]):
					temp = self.heap[index]
					self.heap[index] = rightVal
					self.heap[rightIndex] = temp
					index = rightIndex
				else:
					break
			else:
				break
		self.addIndex -= 1
		return value
	
	def printHeap(self):
		leftVal = 0
		rightVal = 0
		for i in range(len(self.heap)):
			leftIndex = (i*2) + 1
			rightIndex = (i*2) + 2
			if(rightIndex < len(self.heap)):
				leftVal = self.heap[leftIndex]
				rightVal = self.heap[rightIndex]
			else:
				leftVal = None
				rightVal = None
			print(str(self.heap[i]) + "->" + str(leftVal) + "," +str(rightVal))

if __name__ == "__main__":
	h = Heap()
	for i in range(5, 0, -1):
		if(i%2 == 0):
			h.insert(i*300)
		else:
			h.insert(i+1)
		h.printHeap()
		print(" ")
	for i in range(0, len(h.heap)-1):
		print("value", h.removeMin())	
		h.printHeap()
		print(" ")
