from utils import get_neighbors, get_goal_state

def dls(state, goal, depth, path, visited, size):
    if state == goal:
        return path, len(path), visited
    if depth == 0:
        return None, -1, visited  #retorna os visitados mesmo quando a profundidade é 0

    visited.add(state)
    for neighbor, action in get_neighbors(state, size):
        if neighbor not in visited:
            result_path, result_depth, result_visited = dls(neighbor, goal, depth - 1, path + [action], visited, size)
            if result_path:
                return result_path, result_depth, result_visited
    return None, -1, visited

def ids(start_state: tuple, size: int, max_depth=50):
    goal = get_goal_state(size)
    for depth in range(max_depth):
        visited = set()
        path, path_len, visited = dls(start_state, goal, depth, [], visited, size)
        if path:
            return path, path_len, len(visited)
    return None, -1, len(visited)
