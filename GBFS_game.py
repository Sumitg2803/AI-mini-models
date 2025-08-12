from queue import PriorityQueue

# Directions: up, down, left, right
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def gbfs_game(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    pq = PriorityQueue()
    pq.put((heuristic(start, goal), start))
    
    while not pq.empty():
        h, current = pq.get()
        print(f"Visiting: {current}")
        
        if current == goal:
            print("Goal reached!")
            return
        
        visited.add(current)
        
        for move in moves:
            new_r, new_c = current[0] + move[0], current[1] + move[1]
            if (0 <= new_r < rows and 0 <= new_c < cols and
                grid[new_r][new_c] != '#' and
                (new_r, new_c) not in visited):
                pq.put((heuristic((new_r, new_c), goal), (new_r, new_c)))

# Game Grid
grid = [
    ['S', '.', '.', '.', '.'],
    ['.', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (4, 4)

gbfs_game(grid, start, goal)
