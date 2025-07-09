from utils import get_neighbors, get_goal_state

def dfs(start_state: tuple, size: int, limit=50):
    visited = set()
    visited.add(start_state)
    path_map = {start_state: []}  # Mapeia o estado para o caminho até ele
    depth_map = {start_state: 0}  # Mapeia o estado para sua profundidade
    goal = get_goal_state(size)
    expanded_nodes = 0

    while stack:
        state = stack.pop()
        expanded_nodes += 1

        if state == goal:
            return path_map[state], depth_map[state], expanded_nodes

        if depth_map[state] < limite:
            for neighbor, action in reversed(get_neighbors(state, size)):
                if neighbor not in visited:
                    visited.add(neighbor)
                    path_map[neighbor] = path_map[state] + [action]
                    depth_map[neighbor] = depth_map[state] + 1
                    stack.append(neighbor)

    return [], 0, expanded_nodes



