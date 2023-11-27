#!/usr/bin/python3
""" Placing N non-attacking queens on an NN chessboard. """
import sys


matrix = []  # global variables
board = []  # global variables


def result():
    """ Prints result. """
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:  # if a queen is met
                matrix[row][1] = col  # matrix stores the column
    return matrix


def backtrack(r, n, col, posDiag, negDiag):
    """ Recursive function. """
    global board
    if r == n:  # end of row
        print(result())  # print solution
        return

    for c in range(n):
        # checks if the queen can be in given column without
        # attacking other queens, it also checks the positive
        # and negative diagonals. If an attack is possible, it
        # goes to the next column until the end of the row or
        # there is no possible attack.
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue

        # adds the row combinations to the set
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        # board is updated to 1 to indicate that a queen
        # is present in that position
        board[r][c] = 1

        # the function moves to the next row and runs again
        backtrack(r + 1, n, col, posDiag, negDiag)

        # in the event that a queen can't be placed in any column,
        # backtracking happens and the previous queen is moved
        # hence the combinations of the previous queen need to be
        # reset to 0
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        # board is updated to 0 to indicate that a queen
        # is no longer in that position
        board[r][c] = 0


def solve_n_queens(n):
    """ Solve N Queens. """
    col = set()
    posDiag = set()
    negDiag = set()

    global matrix
    global board
    matrix = [[c + r for c in range(2)] for r in range(n)]
    board = [[0 for i in range(n)] for i in range(n)]

    # call backtrack to place our queens
    backtrack(0, n, col, posDiag, negDiag)


if len(sys.argv) != 2:  # wrong number of arguments
    print("Usage: nqueens N")
    sys.exit(1)

num = sys.argv[1]

try:
    num_int = int(num)
except ValueError:  # N must be an int
    print("N must be a number")
    sys.exit(1)

if num_int < 4:  # N must be greater than or equal to 4
    print("N must be at least 4")
    sys.exit(1)

solve_n_queens(num_int)
