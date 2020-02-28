'''
Returns True if knights are placed on a chessboard such that no knight can capture another knight.
Board is assumed to be well-formed.
0's represent empty squares, 1's represent knights.
cannot_capture([
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0]
]) -> True

cannot_capture([
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1]
]) -> False
'''


def cannot_capture(board):
    for x in range(0, 8):
        for y in range(0, 8):
            if board[x][y] == 1 and check_all(board, x, y):
                return False
    return True


def check_all(board, x, y):
    return (check_top_left(board, x, y) or check_top_right(board, x, y) or
            check_left_top(board, x, y) or check_left_bottom(board, x, y) or
            check_bottom_left(board, x, y) or check_bottom_right(board, x, y) or
            check_right_top(board, x, y) or check_right_bottom(board, x, y))


def check_top_left(board, x, y):
    return x > 1 and y > 0 and board[x - 2][y - 1] == 1


def check_top_right(board, x, y):
    return x > 1 and y < 7 and board[x - 2][y + 1] == 1


def check_left_top(board, x, y):
    return x > 0 and y > 1 and board[x - 1][y - 2] == 1


def check_left_bottom(board, x, y):
    return x < 7 and y > 1 and board[x + 1][y - 2] == 1


def check_bottom_left(board, x, y):
    return x < 6 and y > 0 and board[x + 2][y - 1] == 1


def check_bottom_right(board, x, y):
    return x < 6 and y < 7 and board[x + 2][y + 1] == 1


def check_right_top(board, x, y):
    return x > 0 and y < 6 and board[x - 1][y + 2] == 1


def check_right_bottom(board, x, y):
    return x < 7 and y < 6 and board[x + 1][y + 2] == 1


test_board_true = [
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0]
]

test_board_false = [
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1]
]

print(cannot_capture(test_board_true))
print(cannot_capture(test_board_false))
