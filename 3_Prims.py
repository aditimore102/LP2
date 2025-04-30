import heapq

def prims_algorithm(graph, start_node):
    visited = set()
    min_heap = [(0, start_node)]  # (weight, node)
    total_cost = 0
    mst_edges = []

    while min_heap:
        cost, u = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            total_cost += cost
            if cost != 0:  # To avoid printing start node's edge (0 cost)
                mst_edges.append((prev, u, cost))

            for v, weight in graph.get(u, []):
                if v not in visited:
                    heapq.heappush(min_heap, (weight, v))
            
            prev = u  # store the last node
    
    return total_cost, mst_edges

# User Input
graph = {}
nodes = set()

n = int(input("Enter number of edges: "))
print("Enter each edge in the format 'node1 node2 cost':")

for _ in range(n):
    u, v, cost = input().split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))
    nodes.add(u)
    nodes.add(v)

start_node = input("\nEnter the starting node: ")

# Run Prim's algorithm
total_cost, mst_edges = prims_algorithm(graph, start_node)

# Output
print("\nMinimum Spanning Tree edges:")
for u, v, cost in mst_edges:
    print(f"{u} -- {v} == {cost}")

print(f"\nTotal cost of MST: {total_cost}")
