import pygame as p
from config import *
from computer_player import *
from draw import *
from tkinter import *
from PIL import ImageTk, Image
import ast
import operator

def window_game():
    pygame.init()

    screen = draw_screen1()

    board = new_board()
    pygame.display.update()
    pygame.display.set_caption('Caro game')

    game_over = False

    while True:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if game_over:
                    pygame.quit()
                pos = pygame.mouse.get_pos()
                x = pos[0] // 40
                y = pos[1] // 40
                if board[x][y] != 0:
                    continue
                drawX(screen, x, y)
                board[x][y] = 1
                if check_end_game(screen, board):
                    pygame.display.update()
                    ev1 = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()
                computer_reply(screen, board, x, y)
                if check_end_game(screen, board):
                    pygame.display.update()
                    ev = pygame.event.get()
                    game_over = True
                    continue

                pygame.display.update()

window_game()