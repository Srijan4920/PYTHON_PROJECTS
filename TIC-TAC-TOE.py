import pygame
import sys

# --- Pygame setup ---
pygame.init()
WIDTH = 600
ROWS = COLS = 3
SQSIZE = WIDTH // COLS
LINE_WIDTH = 15
CIRCLE_RADIUS = SQSIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 20
OFFSET = 50

# --- Colors ---
BG_COLOR = (28, 28, 28)
LINE_COLOR = (255, 255, 255)
CIRCLE_COLOR = (0, 255, 255)
CROSS_COLOR = (255, 0, 127)

# --- Initialize screen ---
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Tic-Tac-Toe with AI")
screen.fill(BG_COLOR)

# --- Global variables ---
board = [["" for _ in range(COLS)] for _ in range(ROWS)]
game_over = False
human = "X"
ai = "O"

# --- Drawing functions ---
def draw_lines():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQSIZE), (WIDTH, i * SQSIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * SQSIZE, 0), (i * SQSIZE, WIDTH), LINE_WIDTH)

def draw_figures():
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                start = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)
                end = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                pygame.draw.line(screen, CROSS_COLOR, start, end, CROSS_WIDTH)
                start = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)
                end = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)
                pygame.draw.line(screen, CROSS_COLOR, start, end, CROSS_WIDTH)

# --- Game logic ---
def available_moves():
    return [(r, c) for r in range(ROWS) for c in range(COLS) if board[r][c] == ""]

def check_winner():
    # Rows, columns, diagonals
    for r in range(ROWS):
        if board[r][0] == board[r][1] == board[r][2] != "":
            return board[r][0]
    for c in range(COLS):
        if board[0][c] == board[1][c] == board[2][c] != "":
            return board[0][c]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_draw():
    return all(cell != "" for row in board for cell in row)

# --- Minimax Algorithm ---
def minimax(is_maximizing):
    winner = check_winner()
    if winner == ai:
        return 1, None
    elif winner == human:
        return -1, None
    elif is_draw():
        return 0, None

    if is_maximizing:
        max_eval = -float("inf")
        best_move = None
        for (r, c) in available_moves():
            board[r][c] = ai
            eval, _ = minimax(False)
            board[r][c] = ""
            if eval > max_eval:
                max_eval = eval
                best_move = (r, c)
        return max_eval, best_move
    else:
        min_eval = float("inf")
        best_move = None
        for (r, c) in available_moves():
            board[r][c] = human
            eval, _ = minimax(True)
            board[r][c] = ""
            if eval < min_eval:
                min_eval = eval
                best_move = (r, c)
        return min_eval, best_move

def ai_move():
    _, move = minimax(True)
    if move:
        board[move[0]][move[1]] = ai

def restart():
    global board, game_over
    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    game_over = False
    screen.fill(BG_COLOR)
    draw_lines()

# --- Initial draw ---
draw_lines()

# --- Main Loop ---
player_turn = True  # Human starts first
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if not game_over:
            if player_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // SQSIZE
                col = x // SQSIZE
                if board[row][col] == "":
                    board[row][col] = human
                    winner = check_winner()
                    if winner or is_draw():
                        game_over = True
                    else:
                        player_turn = False

        if not player_turn and not game_over:
            ai_move()
            winner = check_winner()
            if winner or is_draw():
                game_over = True
            else:
                player_turn = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player_turn = True

    draw_figures()
    pygame.display.update()
