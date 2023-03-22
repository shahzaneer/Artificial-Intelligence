def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

    return visited


if __name__ == '__main__':
    print("Recursive DFS")
    
    graph = {
    'A': {'B', 'C'},
    'B': {'A', 'D', 'E'},
    'C': {'A', 'F'},
    'D': {'B'},
    'E': {'B', 'F'},
    'F': {'C', 'E'}
}

result = dfs_recursive(graph, 'A')
print(result)

        