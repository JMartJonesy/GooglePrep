from node import *

def DFS(start, end):
	stack = [start]
	visited = []

	while len(stack) > 0:
		top = stack.pop(0)

		if top.data == end.data:
			visited.append(top)
			return visited
		elif top not in visited:
			visited.append(top)
			if len(top.neighbors) > 0:
				stack = top.neighbors + stack
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
	for path in DFS(node1, node3):
		print(path.data)
