# ----------------------------------------
# Function to check if it's safe to assign a color to vertex `v`
# ----------------------------------------
def is_safe(graph, color, v, colored):
    # Check all vertices adjacent to vertex `v`
    for i in range(len(graph[v])):
        # If vertex `i` is adjacent to `v` and has the same color, return False
        if graph[v][i] == 1 and colored[i] == color:
            return False
    return True  # Safe to assign the color

# ----------------------------------------
# Recursive Backtracking Function
# ----------------------------------------
def backtrack(graph, m, colored, v, assignment):
    # If all vertices are successfully colored, return True
    if v == len(graph):
        return True

    # Try assigning each color from 1 to m
    for c in range(1, m + 1):
        # Check if it's safe to assign the color `c` to vertex `v`
        if is_safe(graph, c, v, colored):
            colored[v] = c  # Assign color to vertex `v`
            assignment.append(c)  # Track color assignment (optional for debugging)

            # Recursively try to color the next vertex
            if backtrack(graph, m, colored, v + 1, assignment):
                return True  # If coloring the next vertex works, we are done

            # Backtrack: undo the color assignment for vertex `v`
            colored[v] = 0
            assignment.pop()  # Remove the last color from the assignment list

    return False  # No valid color found for this vertex (need to backtrack)

# ----------------------------------------
# Function to find the minimum number of colors needed
# ----------------------------------------
def minimum_color(graph):
    num_vertices = len(graph)  # Number of vertices in the graph
    result = float('inf')  # Initialize upper bound for the minimum number of colors
    min_colors = 0  # Store the minimum number of colors found
    colored = [0] * num_vertices  # List to track the color of each vertex
    assignment = []  # Optional list to track the color assignments during the process

    # Try increasing the number of colors from 1 to `num_vertices`
    for m in range(1, num_vertices + 1):
        # Try to color the graph using `m` colors
        if backtrack(graph, m, colored, 0, assignment):
            result = min(result, m)  # Update result if a valid coloring is found
            min_colors = m  # Update the minimum number of colors
            assignment.clear()  # Clear the color assignment list for the next attempt
            break  # Stop at the first valid coloring since we're trying colors from 1 upwards

    return min_colors, colored  # Return the minimum number of colors and the coloring result

# ----------------------------------------
# Example Graph as Adjacency Matrix
# ----------------------------------------
graph = [
    [0, 1, 1, 1],  # Vertex 0 is connected to vertices 1, 2, and 3
    [1, 0, 1, 0],  # Vertex 1 is connected to vertices 0 and 2
    [1, 1, 0, 1],  # Vertex 2 is connected to vertices 0, 1, and 3
    [1, 0, 1, 0],  # Vertex 3 is connected to vertices 0 and 2
]

# Run the algorithm to find the minimum number of colors
min_colors, colored = minimum_color(graph)

# Output results
print("Minimum colors needed:", min_colors)
print("Coloring of vertices:", colored)
