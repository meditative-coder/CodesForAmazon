from collections import defaultdict
 
# This class represents a directed graph
# using adjacency list representation
class Graph:
 
    # Constructor
    def __init__(self, vertices):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = vertices
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def cycle_utility(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        for neighbor in self.graph[node]:
            if visited[neighbor] == False:
                if self.cycle_utility(neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack[node] = False
        return False

    def has_cycle(self):
        visited = [False]*(self.V+1)
        rec_stack = [False]*(self.V+1)
        for node in range(self.V):
            if visited[node] == False:
                if self.cycle_utility(node, visited, rec_stack):
                    return True
        return False
        


 

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
print("Has Cycle, ", g.has_cycle())