
import heapq
from utils import get_neighbors, get_goal_state, manhattan_distance, misplaced_tiles

def astar(start_state: tuple, size: int, heuristic='manhattan'):
    goal = get_goal_state(size)
    visited = set()
    heap = []
    g_score = {start_state: 0}
    h = manhattan_distance if heuristic == 'manhattan' else lambda s, g, sz: misplaced_tiles(s, g)
    heapq.heappush(heap, (h(start_state, goal, size), 0, start_state, []))

    while heap:
        f, g, current, path = heapq.heappop(heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            return path, g, len(visited)

        for neighbor, action in get_neighbors(current, size):
            if neighbor not in visited:
                new_g = g + 1
                heapq.heappush(heap, (new_g + h(neighbor, goal, size), new_g, neighbor, path + [action]))

    return None, -1, len(visited)
