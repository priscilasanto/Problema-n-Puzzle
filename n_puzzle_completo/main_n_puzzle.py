import sys
from bfs import bfs
from dfs import dfs
from ids import ids
from astar import astar
from greedy import greedy

def main():
    print("Escolha o algoritmo:")
    print("1. BFS")
    print("2. DFS")
    print("3. IDS")
    print("4. A*")
    print("5. Greedy")
    choice = input("Opção (1-5): ")

    puzzle_size = int(input("Tamanho do quebra-cabeça (ex: 3 para 8-puzzle): "))
    print("Digite o estado inicial separado por espaços (ex: 1 2 3 4 5 6 7 8 0):")
    start_input = input().strip()
    start_state = tuple(map(int, start_input.split()))

    if len(start_state) != puzzle_size * puzzle_size:
        print("Erro: número incorreto de elementos para o tamanho especificado.")
        return

    if choice == '1':
        result = bfs(start_state, puzzle_size)
    elif choice == '2':
        result = dfs(start_state, puzzle_size)
    elif choice == '3':
        result = ids(start_state, puzzle_size)
    elif choice == '4':
        heuristic = input("Heurística (manhattan/hamming): ")
        result = astar(start_state, puzzle_size, heuristic)
    elif choice == '5':
        heuristic = input("Heurística (manhattan/hamming): ")
        result = greedy(start_state, puzzle_size, heuristic)
    else:
        print("Opção inválida.")
        return

    print("\nResultado:")
    print(result)

if __name__ == "__main__":
    main()
