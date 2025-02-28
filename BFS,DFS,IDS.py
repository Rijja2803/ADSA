class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(1, vertices + 1)}

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):
        visited = [False] * (self.vertices + 1)
        queue = [start]
        visited[start] = True

        print("BFS Traversal: ", end="")
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True
        print()

    def dfs_util(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")

        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = [False] * (self.vertices + 1)
        print("DFS Traversal: ", end="")
        self.dfs_util(start, visited)
        print()

    def dls(self, vertex, target, depth, visited):
        if depth < 0:
            return False
        
        print(vertex, end=" ")
        if vertex == target:
            return True
        
        visited[vertex] = True
        for neighbor in self.adj_list[vertex]:
            if not visited[neighbor]:
                if self.dls(neighbor, target, depth - 1, visited):
                    return True
        visited[vertex] = False  # Allow re-visiting in different depth levels
        return False

    def ids(self, start, target, max_depth):
        for depth in range(max_depth + 1):
            visited = [False] * (self.vertices + 1)
            print(f"\nDepth Level {depth}: ", end="")
            if self.dls(start, target, depth, visited):
                print(f"\nTarget {target} found at depth {depth}")
                return
        print(f"\nTarget {target} not found within depth limit {max_depth}")

# Create the graph
G = Graph(4)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(3, 3)
G.add_edge(3, 4)
G.add_edge(4, 1)

# Perform BFS traversal
G.bfs(1)

# Perform DFS traversal
G.dfs(1)

# Perform IDS traversal
target_node = 4
max_depth = 3
G.ids(1, target_node, max_depth)
