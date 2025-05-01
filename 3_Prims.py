import heapq  # For priority queue (min-heap)

# Function to perform Prim's Algorithm
def prims_algorithm(graph, start_node):
    visited = set()  # Set to track visited nodes
    min_heap = [(0, start_node)]  # Min-heap to store (cost, node)
    total_cost = 0  # Total cost of the Minimum Spanning Tree (MST)
    mst_edges = []  # List to store edges in MST

    while min_heap:
        cost, u = heapq.heappop(min_heap)  # Get node with minimum edge cost
        if u not in visited:
            visited.add(u)  # Mark node as visited
            total_cost += cost  # Add edge cost to total MST cost
            if cost != 0:
                mst_edges.append((prev, u, cost))  # Add edge to MST (skip first dummy edge)

            # Check all adjacent nodes
            for v, weight in graph.get(u, []):
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))  # Push edge to heap if the node is not visited
            
            prev = u  # Keep track of the last node for edge trace
    
    return total_cost, mst_edges

# -------------------------
# Input Handling Section
# -------------------------

graph = {}     # Dictionary to store adjacency list
nodes = set()  # Set of all nodes (used to identify unique nodes)

# Read number of edges
n = int(input("Enter number of edges: "))
print("Enter each edge in the format 'node1 node2 cost':")

# Read and store graph edges
for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    # Since the graph is undirected, add both directions
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))
    nodes.add(u)
    nodes.add(v)

# Ask for the starting node for Prim's algorithm
start_node = input("\nEnter the starting node: ")

# Run the algorithm
total_cost, mst_edges = prims_algorithm(graph, start_node)

# -------------------------
# Output Results
# -------------------------

print("\nMinimum Spanning Tree edges:")
for u, v, cost in mst_edges:
    print(f"{u} -- {v} == {cost}")

print(f"\nTotal cost of MST: {total_cost}")
