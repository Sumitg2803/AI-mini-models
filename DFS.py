def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)           # Visit the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

    #     A
    #    / \
    #   B   C
    #  / \    \
    # D   E    G
    #      \
    #       F

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['G'],
    'D': [],
    'E': ['F'],
    'F': [],
    'G': []
}

# Start DFS from node 'A'
dfs(graph, 'A')