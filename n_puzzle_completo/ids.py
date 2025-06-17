
from utils import get_neighbors, get_goal_state

def dls(state, goal, depth, path, visited, size):
    if state == goal:
        return path, len(path), visited
    if depth == 0:
        return None

    visited.add(state)
    for neighbor, action in get_neighbors(state, size):
        if neighbor not in visited:
            result = dls(neighbor, goal, depth - 1, path + [action], visited, size)
            if result:
                return result
    return None

def ids(start_state: tuple, size: int, max_depth=50):
    goal = get_goal_state(size)
    for depth in range(max_depth):
        visited = set()
        result = dls(start_state, goal, depth, [], visited, size)
        if result:
            return result[0], result[1], len(visited)
    return None, -1, len(visited)
