# TAKE-HOME EXAM 1

from collections import deque

graphA = {'A': set(['B']), # ROOT
         'B': set(['A', 'C']),
         'C': set(['B', 'D', 'F']),
         'D': set(['C', 'E']),
         'E': set(['D', 'F']), 
         'F': set(['C', 'E'])} # GOAL

graphB = {'A': set(['B']), # ROOT
         'B': set(['A', 'C']),
         'C': set(['B', 'D']),
         'D': set(['C', 'E']),
         'E': set(['D', 'F']), 
         'F': set(['E'])} # GOAL

graphC = {'A': set(['B', 'C']), # ROOT
         'B': set(['A', 'D']),
         'C': set(['A', 'D']),
         'D': set(['B', 'C', 'E', 'F']),
         'E': set(['D', 'G']), 
         'F': set(['D', 'G']), 
         'G': set(['E', 'F'])} # GOAL

graphD = {'A': set(['B']), # ROOT
         'B': set(['A', 'C']),
         'C': set(['B', 'D']),
         'D': set(['C', 'E', 'G']),
         'E': set(['D', 'F', 'G']), 
         'F': set(['E']), 
         'G': set(['D', 'E'])} # GOAL

graphE = {'A': set(['B']), # ROOT
         'B': set(['A', 'C', 'D']),
         'C': set(['B', 'D']),
         'D': set(['B', 'C', 'E']),
         'E': set(['D']), 
         'F': set(), 
         'G': set(['H', 'I']), 
         'H': set(['G', 'I']),
         'I': set(['G', 'H'])} # GOAL

def BFS(graph, root, goal):
    distance = 0
    queue = deque()

    explored = {root: 0} # explored = map of vertex -> distance
    queue.append( root )

    while len(queue) != 0:
        vertex = queue.popleft()   

        if vertex == goal:
            return explored[vertex]

        for neighbor in graph[vertex]:
            if neighbor not in explored:
                explored[neighbor] = explored[vertex] + 1 # distance(neighbor) = distance(vertex) + 1
                queue.append( neighbor )

    return -1 # not found

if __name__ == "__main__":

    # 1. BFS
    print(f"Graph A Distance Found: { BFS(graphA, 'A', 'F') }") 
    print(f"Graph B Distance Found: { BFS(graphB, 'A', 'F') }")
    print(f"Graph C Distance Found: { BFS(graphC, 'A', 'G') }")
    print(f"Graph D Distance Found: { BFS(graphD, 'A', 'G') }")
    print(f"Graph E Distance Found: { BFS(graphE, 'A', 'G') }")

    # 2. Cocktail