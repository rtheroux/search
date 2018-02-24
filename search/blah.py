path = Stack()
  visited = []
  directions = []

  visited.append(problem.getStartState())
  currentNode = problem.getSuccessors(problem.getStartState())[0]
  path.push(currentNode)
  visited.append(currentNode[0])

  while problem.isGoalState(currentNode[0]) != True:
      allVisited = True
      for node in problem.getSuccessors(currentNode[0]):
          if node[0] not in visited:
              allVisited = False
              currentNode = node
              path.push(currentNode)
              visited.append(currentNode[0])
              break
          else:
              pass
      if allVisited == True:
          if not path.isEmpty():
              path.pop()
              if not path.isEmpty():
                  currentNode = path.list[-1]
          else:
              break

  for node in path.list:
      if node[1] == "South":
          directions.append(s)
      elif node[1] == "North":
          directions.append(n)
      elif node[1] == "East":
          directions.append(e)
      elif node[1] == "West":
          directions.append(w)
  return directions








  from game import Directions
  from util import Queue
  import time
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST

  # searched list of nodes
  fringe = Queue()
  path = []
  visited = []
  directions = []

  path.append(problem.getStartState())
  fringe.push(path)

  currentNode = fringe.list[-1][-1]
  visited.append(currentNode)

  while problem.isGoalState(currentNode) != True:
      for fork in problem.getSuccessors(currentNode):
          if fork[0] not in visited:
              path = list(fringe.list[-1])
              path.append(fork[0])
              fringe.push(path)
              visited.append(fork[0])
      fringe.pop()
      currentNode=fringe.list[-1][-1]

  stack = list(fringe.list[-1])

  for i in range(len(stack) - 1):
      if stack[i][0] > stack[i+1][0]:
          directions.append(w)
      elif stack[i][0] < stack[i+1][0]:
          directions.append(e)
      elif stack[i][1] > stack[i+1][1]:
          directions.append(s)
      elif stack[i][1] < stack[i+1][1]:
          directions.append(n)

  return directions
