import pygame
import sys

# Khai báo các hằng số
BOARD_SIZE = 15
CELL_SIZE = 40
SCREEN_SIZE = BOARD_SIZE * CELL_SIZE

# Màu sắc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def draw_board(screen):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            pygame.draw.rect(screen, WHITE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
            pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Caro Game")
    
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)
        draw_board(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
