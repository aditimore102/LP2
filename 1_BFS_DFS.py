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
def main():
    graph = {}
    n = int(input("Enter number of edges: "))

    print("Enter edges (format: node1 node2):")
    for _ in range(n):
        u, v = input().split()
        add_edge(graph, u, v)

    start_node = input("Enter starting node for DFS and BFS: ")

    print("\nDFS Traversal:")
    dfs(graph, start_node, set())

    print("\n\nBFS Traversal:")
    bfs(graph, start_node)

if __name__ == "__main__":
    main()





