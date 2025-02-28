class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])  # Path compression
        return self.parent[v]

    def union(self, u, v):
        self.parent[self.find(u)] = self.find(v)  # Simple union

def kruskal(edges, n):
    ds = DisjointSet(n)
    edges.sort(key=lambda x: x[2])  # Sorting edges by weight
    mst = []
    total_weight = 0  

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):  # If they belong to different sets
            ds.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight  

    return mst, total_weight

# Example Usage
edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]
n = 4  # Number of vertices

mst, total_weight = kruskal(edges, n)
print("Minimum Spanning Tree:", mst)
print("Total Weight:", total_weight)
