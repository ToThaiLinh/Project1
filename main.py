import pygame as p
from config import *
from computer_player import *
from draw import *
from tkinter import *
from PIL import ImageTk, Image
import ast
import operator

def main():
    global screen_size
    screen_size = (400, 400)
    p.init()
    screen = p.display.set_mode(screen_size, p.RESIZABLE)
    screen.fill(screen_color)
    img = p.image.load('image/icon.png')
    p.display.set_icon(img)
    p.display.set_caption('Caro game')
    draw_board(screen, screen_size[0], screen_size[1])
    board = new_board(screen_size[0], screen_size[1])
    p.display.update()
    clock = p.time.Clock()

    gameOver = False

    running = True

    while running:
        events = p.event.get()
        for event in events:
            if event.type == p.QUIT:
                running = False

            elif event.type == p.VIDEORESIZE:
                screen_size = event.size
                screen_size = ((screen_size[0] // square_size) * square_size, (screen_size[1] // square_size) * square_size)
                screen = p.display.set_mode(screen_size, p.RESIZABLE)
                screen.fill(screen_color)
                draw_board(screen, screen_size[0], screen_size[1])
                board = new_board(screen_size[0], screen_size[1])

            elif event.type == p.MOUSEBUTTONUP:
                if not gameOver:
                    location = p.mouse.get_pos()
                    col = location[0] // square_size
                    row = location[1] // square_size
                    
                    if board[col][row] != 0:
                        continue
                    print(row, col)
                    drawX(screen, col, row)
                    board[col][row] = 1
                    print(board[col][row])
                    if check_end_game(screen, board):
                        p.display.update()
                        gameOver = True
                        continue
                    p.display.update()
                    computer_reply(screen, board, col, row)
                    if check_end_game(screen, board):
                        p.display.update()
                        events = p.event.get()
                        gameOver = True
                        continue
                    p.display.update()

        draw_board(screen, screen_size[0], screen_size[1])           
        p.display.update()
        clock.tick(30)
    p.quit()

if __name__ == '__main__':
    main()