#class for nodes for a* algorithm
class Node(object):
	def __init__(self, parent=None, currentPos=None):
		self.parent = parent
		self.currentPos = currentPos

		self.f = 0
		self.g = 0
		self.h = 0
	
	def __eq__(self, other):
		return self.currentPos == other.currentPos

def gameMode_pathFinder(map, start, target):
	#uses a* algorithm

	#establish 2 lists; one has nodes that hasn't been examined; other has nodes that have been examined
	openList = []
	closedList = []

	#establish start and end nodes (where we are beginning and where we want to end up)
	startingNode = Node(None, start)
	startingNode.f = 0
	startingNode.g = 0
	startingNode.h = 0

	endNode = Node(None, target)
	endNode.f = 0
	endNode.g = 0
	endNode.h = 0

	#append the starting node to the open list
	openList.append(startingNode)

	while len(openList) > 0:
		currentNode = openList[0]
		currentIndex = 0
		for i in range(len(openList)):
			if openList[i].f < currentNode.f:
				currentNode = openList[i]
				currentIndex = i

		openList.pop(currentIndex)
		closedList.append(currentNode)

		if currentNode == endNode:
			solution = []
			current = currentNode
			while current is not None:
				solution.append(current.currentPos)
				current = current.parent
			return solution[::-1]

		children = []
		#possible moves
		nextMoves = [(0,1), (0,-1), (-1,0), (1,0)]

		for move in nextMoves:
			newX = currentNode.currentPos[0] + move[0]
			newY = currentNode.currentPos[1] + move[1]

			if (newX >= len(map)) or (newX < 0) or\
				(newY >= len(map[0])) or (newY < 0):
				continue

			if map[newX][newY] != 0:
				continue

			newNode = Node(currentNode, (newX, newY))

			children.append(newNode)
		
		for childNode in children:
			for closedNode in closedList:
				if closedNode == childNode:
					continue
			
			childNode.g = currentNode.g + 1
			#pythag thm to calculate distance bt current node to end node
			childNode.h = (childNode.currentPos[0] - endNode.currentPos[0])**2 +\
				(childNode.currentPos[1] - endNode.currentPos[1])**2
			childNode.f = childNode.g + childNode.h

			for openNode in openList:
				if childNode == openNode and childNode.g > openNode.g:
					continue
			
			openList.append(childNode)