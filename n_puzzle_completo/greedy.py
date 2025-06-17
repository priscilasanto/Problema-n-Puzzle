
import heapq
from utils import get_neighbors, get_goal_state, manhattan_distance, misplaced_tiles

def greedy(start_state: tuple, size: int, heuristic='manhattan'):
    goal = get_goal_state(size)
    visited = set()
    heap = []
    h = manhattan_distance if heuristic == 'manhattan' else lambda s, g, sz: misplaced_tiles(s, g)
    heapq.heappush(heap, (h(start_state, goal, size), start_state, []))

    while heap:
        h_val, current, path = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, len(path), len(visited)

        for neighbor, action in get_neighbors(current, size):
            if neighbor not in visited:
                heapq.heappush(heap, (h(neighbor, goal, size), neighbor, path + [action]))

    return None, -1, len(visited)
