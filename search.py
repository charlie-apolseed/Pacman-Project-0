# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    stack = util.Stack()
    
    # Stack keeps track of possible states as well as path to reach them
    stack.push((problem.getStartState(), []))
    visited = set()
    while not stack.isEmpty():
        # Continue until there are no unvisited states and goal has not been reached
        currentState, path = stack.pop()
        if problem.isGoalState(currentState):
            return path
        if currentState in visited:
            continue
        visited.add(currentState)
        for successor in problem.getSuccessors(currentState):
            if successor[0] not in visited:
                stack.push((successor[0], path + [successor[1]]))
    
    # Return empty list if no solution is found
    return []



def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    # Stack keeps track of possible states as well as path to reach them
    queue.push((problem.getStartState(), []))
    visited = set()
    while not queue.isEmpty():
        # Continue until there are no unvisited states and goal has not been reached
        currentState, path = queue.pop()
        if problem.isGoalState(currentState):
            return path
        if currentState in visited:
            continue
        visited.add(currentState)
        for successor in problem.getSuccessors(currentState):
            if successor[0] not in visited:
                queue.push((successor[0], path + [successor[1]]))
    
    # Return empty list if no solution is found
    return []



def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """
    "*** YOUR CODE HERE ***"
    """
    This is an implementation of UCS. It searches the nodes in order of 
    increasing cost, where the cost is calculated using the built in 
    getCostOfActions function.
    """
    pqueue = util.PriorityQueue()
    #Initialize pqueue
    pqueue.push((problem.getStartState(), []), problem.getCostOfActions([]))
    #Keep track of visited locations
    visited = set()
    #Continue until the goal is reached or the Pqueue is empty
    while not pqueue.isEmpty():
        currentState, path= pqueue.pop()
        #Check for goal
        if problem.isGoalState(currentState):
            return path
        #Check if it has been visited
        if currentState in visited:
            continue
        visited.add(currentState)
        #Add all successors with their priority being the estimated cost.
        for successor in problem.getSuccessors(currentState):
            if successor[0] not in visited:
                newPath = path + [successor[1]]
                pqueue.push((successor[0], newPath), problem.getCostOfActions(newPath))
    
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    "*** YOUR CODE HERE ***"
    """
    This is an implementation of the A* search algorithm. It uses a priority queue to manage the 
    order to search nodes, and the priority is given by taking the sum of the number of steps leading 
    to the current position with the heurisitic value for the next move.
    """
    pqueue = util.PriorityQueue()
    #Initialize the priority queue with the start state
    pqueue.push((problem.getStartState(), []), problem.getCostOfActions([]) + heuristic(problem.getStartState(), problem = problem))
    #Keep track of the locations that have been visited
    visited = set()
    #Continue until the goal is reached or the Pqueue is empty
    while not pqueue.isEmpty():
        currentState, path= pqueue.pop()
        #Check for goal
        if problem.isGoalState(currentState):
            return path
        #Check if visited
        if currentState in visited:
            continue
        visited.add(currentState)
        for successor in problem.getSuccessors(currentState):
            if successor[0] not in visited:
                newPath = path + [successor[1]]
                #Add the new location, the new path, and the estimated cost to the Pqeueue
                pqueue.push((successor[0], newPath), problem.getCostOfActions(newPath) + heuristic(successor[0], problem = problem))
    
    util.raiseNotDefined()



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
