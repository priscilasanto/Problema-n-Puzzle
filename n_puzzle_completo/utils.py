
from typing import List, Tuple

def print_puzzle(state: Tuple[int], size: int) -> None:
    for i in range(size):
        print(state[i * size:(i + 1) * size])
    print()

def get_goal_state(size: int) -> Tuple[int]:
    return tuple(list(range(1, size * size)) + [0])

def get_neighbors(state: Tuple[int], size: int) -> List[Tuple[Tuple[int], str]]:
    neighbors = []
    zero_index = state.index(0)
    row, col = divmod(zero_index, size)

    def swap_and_create(new_row, new_col, action):
        if 0 <= new_row < size and 0 <= new_col < size:
            new_index = new_row * size + new_col
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            neighbors.append((tuple(new_state), action))

    swap_and_create(row - 1, col, 'Up')
    swap_and_create(row + 1, col, 'Down')
    swap_and_create(row, col - 1, 'Left')
    swap_and_create(row, col + 1, 'Right')

    return neighbors

def misplaced_tiles(state: Tuple[int], goal: Tuple[int]) -> int:
    return sum(1 for i, val in enumerate(state) if val != 0 and val != goal[i])

def manhattan_distance(state: Tuple[int], goal: Tuple[int], size: int) -> int:
    distance = 0
    for num in range(1, size * size):
        i, j = state.index(num), goal.index(num)
        x1, y1 = divmod(i, size)
        x2, y2 = divmod(j, size)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
