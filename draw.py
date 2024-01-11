import pygame as p
import sys
import math
from config import *
from position import *

def draw_board(screen, width, height):
    #screen.fill(screen_color)
    for i in range(0, width, square_size):
        p.draw.line(screen, screen_border_color, (i, 0), (i, height), border_thickness)

    for i in range(0, height, square_size):
        p.draw.line(screen, screen_border_color, (0, i), (width, i), border_thickness)

def draw_piece(screen, board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                drawX(screen, j, i)
            elif board[i][j] == -1:
                drawO(screen, j, i)
            elif board[i][j] == 0:
                pass
def drawX(screen, x , y): #x la so cot, y la so hang
    points = ((x * square_size + from_border, y * square_size + from_border), 
             ((x + 1) * square_size - from_border, (y + 1) * square_size - from_border), 
             ((x + 1) * square_size - from_border, y * square_size + from_border), 
             (x * square_size + from_border, (y + 1) * square_size - from_border))
    p.draw.line(screen, X_color, points[0], points[1], tic_tac_thickness)
    p.draw.line(screen, X_color, points[2], points[3], tic_tac_thickness)

def drawO(screen, x, y):
    p.draw.circle(screen, O_color, ((x + 0.5) * square_size, (y + 0.5) * square_size), square_size // 3.14, tic_tac_thickness) 

def new_board(width, height):
    board = [[0 for x in range(width // square_size)] for y in range(height // square_size)]
    return board

#can xem xet
def display_text(screen, text, coordinate):
    font = p.font.Font(text_font, text_size)
    screen_text = font.render(text, True, text_color)
    textRect = screen_text.get_rect()
    textRect.center = (coordinate[0], coordinate[1])
    screen.blit(screen_text, textRect)

def win(screen, winner = "Player"):
    if winner == "Player":
        display_text(screen, win_text, (screen_size[0] // 2 , screen_size[1] //2 ))
    elif winner == "Computer":
        display_text(screen, lose_text, (screen_size[0] // 2, screen_size[1] // 2))
    else:
        display_text(screen, tie_text, (screen_size[0] // 2, screen_size[1] // 2))

def check_end_game(screen, board):
    if enemy_five_in_a_row(board, 1):
        win(screen, "Player")
        return True
    elif enemy_five_in_a_row(board, -1):
        win(screen, "Computer")
        return True
    return False