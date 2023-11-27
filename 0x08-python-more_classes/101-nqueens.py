#!/bin/python3

def solveNQueens(n):
    def could_place(row, col):
        for i in range(row):
            if board[i] == col or \
                board[i] - i == col - row or \
                board[i] + i == col + row:
                return False
        return True

    def place_queens(n, row):
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                place_queens(n, row + 1)
                board[row] = 0

    result = []
    board = [0] * n
    place_queens(n, 0)
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]
