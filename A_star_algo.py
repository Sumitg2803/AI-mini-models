from heapq import heappush, heappop

# 1️⃣ Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# 2️⃣ A* function
def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    # Priority queue (open list): stores (f, node)
    open_list = []
    heappush(open_list, (0, start))  # Push start with f=0 for now

    came_from = {}  # To reconstruct the path
    g_score = {start: 0}  # g(start) = 0

    while open_list:
        # Get node with smallest f
        current_f, current = heappop(open_list)

        # If goal found → reconstruct path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse to get start→goal

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                # Skip walls
                if grid[neighbor[0]][neighbor[1]] == "#":
                    continue

                # g score for this neighbor
                tentative_g = g_score[current] + 1

                # If new path to neighbor is better
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heappush(open_list, (f_score, neighbor))

    return None  # No path found

# 3️⃣ Our same example grid
grid = [
    ["S", ".", "#", ".", "."],
    [".", ".", "#", ".", "."],
    [".", ".", "#", ".", "."],
    ["#", ".", ".", ".", "."],
    [".", ".", ".", ".", "G"]
]

start = (0, 0)
goal = (4, 4)

path = astar(grid, start, goal)
print("Shortest Path:", path)
