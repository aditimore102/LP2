from collections import deque

# Function to add an edge to the graph
def add_edge(graph, u, v):
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)  # Since undirected

# Recursive DFS function
def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS function
def bfs(graph, start):
    visited = set()
    queue = deque()
    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Main program



