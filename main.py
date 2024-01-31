import pygame as p
from config import *
from draw import *
from tkinter import *
from PIL import ImageTk, Image
from CaroAI import *
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
    playerOne = True    # người
    playerTwo = False   # Máy 
    xMove = True

    running = True

    while running:
        humanTurn = (xMove and playerOne) or (not xMove and playerTwo)

        events = p.event.get()
        for event in events:
            if event.type == p.QUIT:
                running = False

            elif event.type == p.VIDEORESIZE:
                screen_size = event.size
                screen_size = ((screen_size[0] // square_size) * square_size, (screen_size[1] // square_size) * square_size)
                screen = p.display.set_mode(screen_size, p.RESIZABLE)
                screen.fill(screen_color)
                old_board = coppyList(board)
                draw_board(screen, screen_size[0], screen_size[1])
                board = new_board(screen_size[0], screen_size[1])
                for i in range(len(board)):
                    for j in range(len(board[0])):
                        #board[i][j] = old_board[i][j]
                        pass
            elif event.type == p.MOUSEBUTTONUP:
                if not gameOver and humanTurn:
                    location = p.mouse.get_pos()
                    col = location[0] // square_size
                    row = location[1] // square_size
                    
                    if board[row][col] != 0:
                        continue
                    print(row, col)
                    drawX(screen, col, row)
                    board[row][col] = 1
                    humanTurn = False
                    if check_end_game(screen, board):
                        p.display.update()
                        gameOver = True
                        continue

        if not humanTurn and not gameOver:
            p.display.update()
            computerMove(screen, board)
            humanTurn = True
            if check_end_game(screen, board):
                p.display.update()
                events = p.event.get()
                gameOver = True
                continue
            p.display.update()
        #draw_board(screen, screen_size[0], screen_size[1])           
        p.display.update()
        clock.tick(30)
    p.quit()

if __name__ == '__main__':
    main()