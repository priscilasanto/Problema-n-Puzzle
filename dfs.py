from utils import get_neighbors, get_goal_state

def dfs(start_state: tuple, size: int, limit=50000):
    visited = set()
    stack = [(start_state, [], 0)]
    goal = get_goal_state(size)

    while stack:
        state, path, depth = stack.pop()
        if state in visited or depth > limit:
            continue
        visited.add(state)

        if state == goal:
            return path, depth, len(visited)

        for neighbor, action in reversed(get_neighbors(state, size)):
            if neighbor not in visited:
                stack.append((neighbor, path + [action], depth + 1))

    return None, -1, len(visited)
