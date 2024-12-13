def init_board():
    return [[0 for i in range(8)] for j in range(8)]


def place_queen(board, a, b):
    for x in range(8):
        board[x][b] -= 1
        board[a][x] -= 1

        if 0 <= a + b - x < 8:
            board[a + b - x][x] -= 1
        if 0 <= a - b + x < 8:
            board[a - b + x][x] -= 1

    board[a][b] = 1


def delete_queen(board, a, b):
    for x in range(8):
        board[x][b] += 1
        board[a][x] += 1

        if 0 <= a + b - x < 8:
            board[a + b - x][x] += 1
        if 0 <= a - b + x < 8:
            board[a - b + x][x] += 1

    board[a][b] = 0


def solution(board, a, count):
    for b in range(8):
        if board[a][b] == 0:
            place_queen(board, a, b)

            if a == 7:
                output_position(board)
                count[0] += 1
            else:
                solution(board, a + 1, count)

            delete_queen(board, a, b)


def output_position(board):
    chars = 'abcdefgh'
    positions = []

    for i in range(8):
        for j in range(8):
            if board[i][j] == 1:
                positions.append(chars[j] + str(i + 1))

    print('; '.join(positions))


def main():
    count = [0]
    board = init_board()

    solution(board, 0, count)

    print(f'\nTotal solutions: {count[0]}')


if __name__ == '__main__':
    main()