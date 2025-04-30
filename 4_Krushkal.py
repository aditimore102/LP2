# Helper: Disjoint Set (Union-Find) implementation
class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:
            return False  # Same set, cycle detected
        self.parent[root_v] = root_u
        return True

def kruskals_algorithm(edges, nodes):
    edges.sort(key=lambda x: x[2])  # Sort edges by weight
    ds = DisjointSet(nodes)
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

# User Input
edges = []
nodes = set()

n = int(input("Enter number of edges: "))
print("Enter each edge in the format 'node1 node2 cost':")
for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    edges.append((u, v, cost))
    nodes.add(u)
    nodes.add(v)

# Run Kruskal's algorithm
mst, total_cost = kruskals_algorithm(edges, nodes)

# Output
print("\nMinimum Spanning Tree edges:")
for u, v, cost in mst:
    print(f"{u} -- {v} == {cost}")

print(f"\nTotal cost of MST: {total_cost}")
