from utils import print_puzzle, get_neighbors

import sys
import time # Para medir o tempo de execução

from bfs import bfs
from dfs import dfs
from ids import ids
from astar import astar
from greedy import greedy

# Função para visualizar o caminho do estado inicial até o objetivo
def print_search_path(path, start_state, size):
    state = start_state
    print("\nÁrvore/Caminho da busca:")
    print_puzzle(state, size)
    for move in path:
        for neighbor, action in get_neighbors(state, size):
            if action == move:
                print(f"Ação: {action}")
                print_puzzle(neighbor, size)
                state = neighbor
                break

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
    
    #Inicio da contagem do tempo
    start_time = time.time()

    if choice == '1':
        result = bfs(start_state, puzzle_size)
    elif choice == '2':
        result = dfs(start_state, puzzle_size)
    elif choice == '3':
        result = ids(start_state, puzzle_size)
    elif choice == '4' or choice == '5':
        print("Escolha a heurística: ")
        print("1. Manhattan")
        print("2. Hamming")
        heuristic_choice = input("Opção (1-2): ")
        heuristic = 'manhattan' if heuristic_choice == '1' else 'hamming' if heuristic_choice == '2' else None
        if heuristic is None:
            print("Heurística inválida.")
            return
        if choice == '4':
            result = astar(start_state, puzzle_size, heuristic)
        else:
            result = greedy(start_state, puzzle_size, heuristic)
        
    else:
        print("Opção inválida.")
        return
    
    #Fim da contagem do tempo
    end_time = time.time()
    elapsed_time = end_time - start_time

    #Apresentação dos resultados
    print("\nResultados:")
    if result[0] is None:
        print("Solução não encontrada.")
    else:
        print_search_path(result[0], start_state, puzzle_size)
        print("Movimentos:", result[0])
        print("Profundidade:", result[1])
        print("Nós visitados:", result[2])
        print("Tempo de execução: {:.4f} segundos".format(elapsed_time))


if __name__ == "__main__":
    main()

