BOARD_SIZE = 9
EMPTY = "."
KING = "K"
DEFENDER = "D"
ATTACKER = "A"

# Set up the board
def init_board():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    mid = BOARD_SIZE // 2
    board[mid][mid] = KING

    # Place defenders around the King
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        board[mid + dx][mid + dy] = DEFENDER

    # Place attackers on edges
    for i in [3, 4, 5]:
        board[0][i] = ATTACKER
        board[8][i] = ATTACKER
        board[i][0] = ATTACKER
        board[i][8] = ATTACKER

    return board

# Print the board
def print_board(board):
    print("   " + " ".join(chr(ord('a') + i) for i in range(BOARD_SIZE)))
    for i, row in enumerate(board):
        print(str(i + 1).rjust(2), " ".join(row))

# Parse user input like "e4"
def parse_pos(pos_str):
    col = ord(pos_str[0].lower()) - ord('a')
    row = int(pos_str[1]) - 1
    return row, col

# Move a piece (no rules yet)
def move_piece(board, start, end):
    sx, sy = start
    ex, ey = end
    piece = board[sx][sy]

    if piece == EMPTY:
        print("No piece there.")
        return False

    if board[ex][ey] != EMPTY:
        print("Destination not empty.")
        return False

    # Only allow straight line moves
    if sx != ex and sy != ey:
        print("Can only move in straight lines.")
        return False

    board[ex][ey] = piece
    board[sx][sy] = EMPTY
    return True

# Game loop
def play():
    board = init_board()
    while True:
        print_board(board)
        move = input("Enter move (e.g. e4 e6): ").split()
        if len(move) != 2:
            print("Please enter two positions.")
            continue
        try:
            start = parse_pos(move[0])
            end = parse_pos(move[1])
            move_piece(board, start, end)
        except Exception as e:
            print("Invalid move. Try again.", e)

play()
