from collections import deque

def bfs(graph, start):
    visited = set()          # To keep track of visited nodes
    queue = deque([start])   # Initialize queue with the start node

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)      # Visit the node
            visited.add(node)
            queue.extend(graph[node])  # Add neighbors to the queue

    #     A
    #    / \
    #   B   C
    #  / \    \
    # D   E    F
    #      \
    #       F

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Start BFS from node 'A'
bfs(graph,'A')