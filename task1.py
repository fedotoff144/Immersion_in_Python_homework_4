'''
1. Напишите функцию для транспонирования матрицы.
Пример: [[1, 2, 3], [4, 5, 6]] ->
'''
from typing import List
from numpy import transpose, array, ndarray


def print_matrix(matrix: List[List[int]]) -> None:
    for line in matrix:
        for namber in line:
            print(f"{namber} \t", end="")
        print()


def transpose_matrix_v1(matrix: List[List[int]]) -> List[List[int]]:
    transpose_matrix: List[List[int]] = []

    for line in zip(*matrix):
        transpose_matrix.append(list(line))

    return transpose_matrix


def transpose_matrix_v2(matrix: List[List[int]]) -> ndarray:
    return transpose(array(matrix))


matrix = [[1, 2, 3], [4, 5, 6]]

# start

print("\nИсходная матрица:\n")
print_matrix(matrix)

print("\nТранспонированная матрица версия 1:\n")
print_matrix(transpose_matrix_v1(matrix))

print("\nТранспонированная матрица версия 2:\n")
print_matrix(transpose_matrix_v2(matrix))

# stop
