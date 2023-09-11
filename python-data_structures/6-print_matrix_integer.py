#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(0, len(matrix)):
        for number in range(0, len(matrix[row])):
            if number == len(matrix[row]) - 1:
                print("{:d}".format(matrix[row][number]))
            else:
                print("{:d}".format(matrix[row][number]), end=" ")
