import sys

def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i in range(row - 1, -1, -1):
        if board[i][col] == 'Q' and col - row + i >= 0:
            return False

    for i in range(row + 1, len(board)):
        if board[i][col] == 'Q' and col + row - i < len(board):
            return False

    for i in range(row - 1, -1, -1):
        for j in range(col - 1, -1, -1):
            if board[i][j] == 'Q' and col - row + i >= 0 and j - col + row >= 0:
                return False

    for i in range(row + 1, len(board)):
        for j in range(col + 1, len(board)):
            if board[i][j] == 'Q' and col + row - i < len(board) and j - col + row < len(board):
                return False

    return True

def solve(board, row):
    if row == len(board):
        print(''.join(board))
        return

    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            solve(board, row + 1)
            board[row][col] = '.'

def main():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    N = int(sys.argv[1])
    if not isinstance(N, int):
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    board = [['.' for _ in range(N)] for _ in range(N)]
    solve(board, 0)

if __name__ == '__main__':
    main()
