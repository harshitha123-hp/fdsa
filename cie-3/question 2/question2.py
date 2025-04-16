from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)
        

    def bfs(self, start_vertex):
        visited = set()  
        queue = deque([start_vertex])  

        print("BFS Traversal Order:")
        while queue:
            vertex = queue.popleft()  
            if vertex not in visited:
                print(vertex, end=" ")  
                visited.add(vertex)  
                for neighbor in self.adj_list.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)  


g = Graph()


g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.add_edge(4, 7)
g.add_edge(5, 8)


g.bfs(0)
