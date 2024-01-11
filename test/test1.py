import pygame as p
import sys

screen_color = (255, 255, 255)
screen_border_color = (0, 0, 0)
border_thickness = 2
square_size = 50

def draw_board(screen, width, height):
    screen.fill(screen_color)

    for i in range(width):
        for j in range(height):
            rect = p.Rect(i * square_size, j * square_size, square_size, square_size)
            p.draw.rect(screen, screen_border_color, rect, border_thickness)

def draw_screen():
    p.init()
    screen_size = (500, 500)
    screen = p.display.set_mode(screen_size, p.RESIZABLE)
    clock = p.time.Clock()

    running = True

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
            elif event.type == p.VIDEORESIZE:
                screen_size = event.size
                screen_size = ((screen_size[0] // square_size) * square_size, (screen_size[1] // square_size) * square_size)
                screen = p.display.set_mode(screen_size, p.RESIZABLE)

        draw_board(screen, (screen_size[0] // square_size) * square_size, (screen_size[1] // square_size) * square_size)
        p.display.flip()
        clock.tick(30)

    p.quit()

draw_screen()
