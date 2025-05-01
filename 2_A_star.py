import heapq  # For priority queue implementation

# A* Algorithm Implementation
def a_star(graph, heuristics, start, goal):
    # Initialize the open set (priority queue) and add the start node with priority 0
    open_set = []
    heapq.heappush(open_set, (0, start))  # (f_score, node)

    came_from = {}  # To reconstruct the final path
    g_score = {start: 0}  # g_score[start] is 0; others will be added dynamically

    while open_set:
        # Pop the node with the lowest f_score
        _, current = heapq.heappop(open_set)

        # If the goal is reached, reconstruct the path and return it
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse the path

        # Check all the neighbors of the current node
        for neighbor, cost in graph.get(current, []):
            # Calculate the tentative g_score to the neighbor
            tentative_g_score = g_score[current] + cost

            # If this path to neighbor is better than any previous one
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current  # Remember how we got here
                g_score[neighbor] = tentative_g_score  # Update cost to reach neighbor

                # Calculate f_score = g_score + heuristic
                f_score = tentative_g_score + heuristics.get(neighbor, 0)
                heapq.heappush(open_set, (f_score, neighbor))  # Add to open set with priority

    return None  # If no path is found

# -------------------------
# Input Handling Section
# -------------------------

graph = {}       # Adjacency list representation of the graph
heuristics = {}  # Heuristic values for each node

# Take input for nodes
n = int(input("Enter number of nodes: "))
nodes = []
print("Enter node names:")
for _ in range(n):
    node = input().strip()
    nodes.append(node)

# Take heuristic values for each node
print("\nEnter heuristic values:")
for node in nodes:
    heuristics[node] = int(input(f"Heuristic for {node}: "))

# Take input for edges in the graph
e = int(input("\nEnter number of edges: "))
print("Enter edges in format 'from to cost':")
for _ in range(e):
    u, v, cost = input().split()
    cost = int(cost)
    # Since the graph is undirected, add both directions
    graph.setdefault(u, []).append((v, cost))
    graph.setdefault(v, []).append((u, cost))

# Input the start and goal nodes
start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

# Run the A* algorithm
path = a_star(graph, heuristics, start, goal)

# Print the result
if path:
    print("\nPath found:", " -> ".join(path))
else:
    print("\nNo path found.")
