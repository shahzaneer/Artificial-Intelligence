# Assume that the graph is represented as an adjacency list
#! Scallable!
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(graph, start):
    visited = set() #so that repeated elements should not be included twice
    queue = [start] # jahan se start krna hai usse queue main dalna hai
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                queue.append(neighbor)
    return visited

print(bfs(graph, 'A'))
