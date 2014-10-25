from node import *
from collections import deque

def BFSIter(start, end):
	queue = deque([start])
	visited = []

	while len(queue) > 0:
		top = queue.popleft()
		
		if top.data == end.data:
			visited.append(top)
			return visited
		elif top not in visited:
			visited.append(top)
			for neighbor in top.neighbors:
				queue.append(neighbor)
	return visited

if __name__ == "__main__":
	node8 = Node(8)
	node7 = Node(7) 
	node6 = Node(6)
	node5 = Node(5, [node7, node8])
	node4 = Node(4)
	node3 = Node(3, [node6])
	node2 = Node(2, [node4, node5])
	node1 = Node(1, [node2, node3])
	for path in BFSIter(node1, node7):
		print(path.data)
