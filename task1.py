'''
1. Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3], [4, 5, 6]] ->
'''
from typing import List


def print_matrix(matrix: List[List[int]]) -> None:
    for line in matrix:
        for namber in line:
            print(f"{namber} \t", end="")
        print()


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    transpose_matrix: List[List[int]] = []

    for line in zip(*matrix):
        transpose_matrix.append(list(line))

    return transpose_matrix


matrix = [[1, 2, 3], [4, 5, 6]]

# start

print("\nИсходная матрица:\n")
print_matrix(matrix)

print("\nТранспонированная матрица:\n")
print_matrix(transpose_matrix(matrix))

# stop
