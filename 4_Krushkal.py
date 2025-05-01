# ----------------------------
# Disjoint Set (Union-Find) Implementation
# ----------------------------
class DisjointSet:
    def __init__(self, nodes):
        # Initially, each node is its own parent (self-loop)
        self.parent = {node: node for node in nodes}
    
    def find(self, node):
        # Finds the representative (root) of the set containing `node`
        # Uses path compression to flatten the tree
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        # Joins the sets containing `u` and `v`
        root_u = self.find(u)
        root_v = self.find(v)
        
        if root_u == root_v:
            return False  # They are already connected (would form a cycle)
        
        self.parent[root_v] = root_u  # Union the two sets
        return True

# ----------------------------
# Kruskal's Algorithm
# ----------------------------
def kruskals_algorithm(edges, nodes):
    # Step 1: Sort edges by their weights (cost)
    edges.sort(key=lambda x: x[2])  # x[2] is the weight
    ds = DisjointSet(nodes)  # Create a disjoint set for cycle detection
    mst = []  # List to store MST edges
    total_cost = 0  # Total weight of MST

    # Step 2: Loop through all sorted edges
    for u, v, weight in edges:
        if ds.union(u, v):  # If adding edge doesn't form a cycle
            mst.append((u, v, weight))  # Add edge to MST
            total_cost += weight  # Add weight to total cost

    return mst, total_cost

# ----------------------------
# Input Handling
# ----------------------------

edges = []  # List of edges (u, v, weight)
nodes = set()  # Set of unique nodes

# Read number of edges
n = int(input("Enter number of edges: "))
print("Enter each edge in the format 'node1 node2 cost':")
for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    edges.append((u, v, cost))
    nodes.add(u)
    nodes.add(v)

# ----------------------------
# Run the Algorithm
# ----------------------------

mst, total_cost = kruskals_algorithm(edges, nodes)

# ----------------------------
# Output the Results
# ----------------------------

print("\nMinimum Spanning Tree edges:")
for u, v, cost in mst:
    print(f"{u} -- {v} == {cost}")

print(f"\nTotal cost of MST: {total_cost}")
