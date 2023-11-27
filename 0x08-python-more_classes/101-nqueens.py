#!/usr/bin/python3
"""This module contains a program that solves the N queens problem."""

import sys


def is_safe(board, row, col, n):
    """This function checks if a queen can be placed on board[row][col]."""
    # Check the row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check the upper diagonal on the left
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check the lower diagonal on the left
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solve_nq(board, col, n, solutions):
    """This function solves the N queens problem using backtracking."""
    # Base case: If all queens are placed, then return true
    if col == n:
        # Print the solution
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True
    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(n):
        # Check if the queen can be placed on board[i][col]
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1
            # Make result true if any placement is possible
            res = solve_nq(board, col + 1, n, solutions) or res
            # Backtrack: Remove the queen from board[i][col]
            board[i][col] = 0
    # If the queen can not be placed in any row in this column, return false
    return res


def main():
    """This is the main function of the program."""
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # Check the type of argument
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    # Check the value of argument
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    # Create an empty board
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Create a list to store the solutions
    solutions = []
    # Solve the N queens problem
    solve_nq(board, 0, n, solutions)
    # Print the solutions
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
