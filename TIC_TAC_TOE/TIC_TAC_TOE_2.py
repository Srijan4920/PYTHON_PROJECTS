import pygame as pg
import sys
import time
from pygame.locals import *

# Global variables
XO = 'x'
winner = None
draw = False
score = {'x': 0, 'o': 0}

# Display size
width, height = 400, 400
white = (255, 255, 255)
line_color = (0, 0, 0)

# Initialize board
board = [[None]*3, [None]*3, [None]*3]

pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 150), 0, 32)
pg.display.set_caption("Enhanced Tic Tac Toe")

# Load & resize images
x_img = pg.transform.scale(pg.image.load("X_modified.png"), (80, 80))
o_img = pg.transform.scale(pg.image.load("o_modified.png"), (80, 80))


def draw_lines():
    screen.fill(white)
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)


def draw_status():
    global draw
    font = pg.font.Font(None, 36)
    if winner:
        message = winner.upper() + " wins!"
    elif draw:
        message = "Game Draw!"
    else:
        message = XO.upper() + "'s Turn"

    screen.fill((0, 0, 0), (0, height, width, 150))
    msg_text = font.render(message, True, white)
    screen.blit(msg_text, (20, height + 10))

    # Restart button
    pg.draw.rect(screen, (70, 130, 180), (width - 120, height + 30, 100, 40))
    btn_font = pg.font.Font(None, 24)
    btn_text = btn_font.render("Restart", True, white)
    screen.blit(btn_text, (width - 100, height + 40))

    pg.display.update()


def check_win():
    global winner, draw

    # Rows & Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            winner = board[i][0]
            pg.draw.line(screen, (255, 0, 0), (0, i * height / 3 + height / 6),
                         (width, i * height / 3 + height / 6), 4)
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            winner = board[0][i]
            pg.draw.line(screen, (255, 0, 0), (i * width / 3 + width / 6, 0),
                         (i * width / 3 + width / 6, height), 4)

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        winner = board[0][0]
        pg.draw.line(screen, (255, 0, 0), (50, 50), (350, 350), 4)

    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        winner = board[0][2]
        pg.draw.line(screen, (255, 0, 0), (350, 50), (50, 350), 4)

    if all(all(row) for row in board) and not winner:
        draw = True

    draw_status()


def drawXO(row, col):
    global XO
    if board[row][col] is None:
        board[row][col] = XO
        x_pos = col * width / 3 + 30
        y_pos = row * height / 3 + 30
        screen.blit(x_img if XO == 'x' else o_img, (x_pos, y_pos))
        XO = 'o' if XO == 'x' else 'x'
        check_win()
        pg.display.update()


def user_click(pos):
    global XO, draw, winner
    x, y = pos

    if y > height:
        # Restart button
        if width - 120 <= x <= width - 20 and height + 30 <= y <= height + 70:
            reset_game()
        return

    row = int(y // (height / 3))
    col = int(x // (width / 3))
    if board[row][col] is None and not winner:
        drawXO(row, col)


def reset_game():
    global board, XO, winner, draw
    board = [[None]*3 for _ in range(3)]
    XO = 'x'
    winner = None
    draw = False
    draw_lines()
    draw_status()


# Game loop
reset_game()
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click(pg.mouse.get_pos())

    pg.display.update()
    CLOCK.tick(fps)
