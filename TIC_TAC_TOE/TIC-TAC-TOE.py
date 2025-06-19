import pygame as pg
import sys
import time
from pygame.locals import *

# Global variables
XO = 'x'
winner = None
draw = False
width, height = 400, 400
white = (255, 255, 255)
line_color = (0, 0, 0)
board = [[None] * 3 for _ in range(3)]

# Initialize pygame
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

# Load images
try:
    initiating_window = pg.image.load("modified_cover.png")
    initiating_window = pg.transform.scale(initiating_window, (width, height + 100))

    def game_start_screen():
        screen.blit(initiating_window, (0, 0))
        pg.display.update()
        time.sleep(3)
except:
    def game_start_screen():
        screen.fill(white)
        pg.display.update()

x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))

def draw_status():
    global draw
    font = pg.font.Font(None, 40)

    if winner:
        message = f"{winner.upper()} Wins!"
    elif draw:
        message = "Game Draw!"
    else:
        message = f"{XO.upper()}'s Turn"

    screen.fill((0, 0, 0), (0, height, width, 100))
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(width // 2, height + 50))
    screen.blit(text, text_rect)
    pg.display.update()

def game_initiating_window():
    screen.fill(white)
    for i in range(1, 3):
        pg.draw.line(screen, line_color, (0, height / 3 * i), (width, height / 3 * i), 7)
        pg.draw.line(screen, line_color, (width / 3 * i, 0), (width / 3 * i, height), 7)
    draw_status()

def drawXO(row, col):
    global XO, board
    posx = (col - 1) * width / 3 + 30
    posy = (row - 1) * height / 3 + 30

    if board[row - 1][col - 1] is None:
        board[row - 1][col - 1] = XO
        if XO == 'x':
            screen.blit(x_img, (posx, posy))
            XO = 'o'
        else:
            screen.blit(o_img, (posx, posy))
            XO = 'x'
        pg.display.update()

def check_win():
    global winner, draw
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0]:
            winner = board[row][0]
            pg.draw.line(screen, (255, 0, 0),
                         (0, row * height / 3 + height / 6),
                         (width, row * height / 3 + height / 6), 4)
            break
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col]:
            winner = board[0][col]
            pg.draw.line(screen, (255, 0, 0),
                         (col * width / 3 + width / 6, 0),
                         (col * width / 3 + width / 6, height), 4)
            break
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        winner = board[0][0]
        pg.draw.line(screen, (255, 0, 0), (30, 30), (width - 30, height - 30), 4)
    elif board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        winner = board[0][2]
        pg.draw.line(screen, (255, 0, 0), (width - 30, 30), (30, height - 30), 4)

    if all(all(cell for cell in row) for row in board) and winner is None:
        draw = True
    draw_status()

def user_click():
    x, y = pg.mouse.get_pos()
    if y < height:
        row = y // (height // 3) + 1
        col = x // (width // 3) + 1
        if board[row - 1][col - 1] is None:
            drawXO(row, col)
            check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(2)
    XO = 'x'
    winner = None
    draw = False
    board = [[None] * 3 for _ in range(3)]
    game_initiating_window()

# Run the game
game_start_screen()
game_initiating_window()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)
