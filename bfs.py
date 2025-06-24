
from collections import deque
from utils import get_neighbors, get_goal_state

def bfs(start_state: tuple, size: int):
    visited = set()
    queue = deque([(start_state, [], 0)])
    goal = get_goal_state(size)

    while queue:
        state, path, depth = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path, depth, len(visited)

        for neighbor, action in get_neighbors(state, size):
            if neighbor not in visited:
                queue.append((neighbor, path + [action], depth + 1))

    return None, -1, len(visited)
