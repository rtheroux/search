# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack
    import time
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    # searched list of nodes
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
                currentNode = path.list[-1]
            else:
                return

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

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

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


def uniformCostSearch(problem):
    from game import Directions
    from util import PriorityQueueWithFunction, Queue
    import time
    s = Directions.SOUTH
    w = Directions.WEST
    n = Directions.NORTH
    e = Directions.EAST

    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # x = PriorityQueueWithFunction(qFunction)
    # x.priorityFunction





def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
