import heapq

# A* Algorithm Implementation
def a_star(graph, heuristics, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))  # Push the start node with priority 0
    
    came_from = {}
    g_score = {start: 0}
    
    while open_set:
        # Pop the node with the lowest f_score
        _, current = heapq.heappop(open_set)

        if current == goal:
            # Reconstruct the path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]
        
        # Explore neighbors
        for neighbor, cost in graph.get(current, []):
            tentative_g_score = g_score[current] + cost
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                
                # Calculate f_score and push to open set
                f_score = tentative_g_score + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (f_score, neighbor))
    
    return None  # No path found

# Input part
graph = {}
heuristics = {}

# Take input for nodes and heuristic values
n = int(input("Enter number of nodes: "))
nodes = []
print("Enter node names:")
for _ in range(n):
    node = input().strip()
    nodes.append(node)

print("\nEnter heuristic values:")
for node in nodes:
    heuristics[node] = int(input(f"Heuristic for {node}: "))

# Take input for edges
e = int(input("\nEnter number of edges: "))
print("Enter edges in format 'from to cost':")
for _ in range(e):
    u, v, cost = input().split()
    cost = int(cost)
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))  # If undirected graph

# Take start and goal node inputs
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Run A* search
path = a_star(graph, heuristics, start, goal)

if path:
    print("\nPath found:", " -> ".join(path))
else:
    print("\nNo path found.")
