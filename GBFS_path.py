from queue import PriorityQueue

def greedy_best_first_search(graph, heuristics, start, goal):
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristics[start], start))
    
    while not pq.empty():
        h, node = pq.get()
        print(f"Visiting: {node}")
        
        if node == goal:
            print("Goal reached!")
            return
        
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                pq.put((heuristics[neighbor], neighbor))
                
#         A(10)
#         /    \
#    B(8)       C(5)
#    / \        / \
#  D(7) E(3)  F(6) G(4)
#      /            \
#    H(2)           I(1)
#                     \
#                     J(0) ← Goal


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H'],
    'F': [],
    'G': ['I'],
    'H': [],
    'I': ['J'],
    'J': []
}

heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 4,
    'H': 2,
    'I': 1,
    'J': 0
}


# Run
greedy_best_first_search(graph, heuristics, 'A', 'J')


