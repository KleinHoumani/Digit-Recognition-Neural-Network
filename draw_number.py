import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 240

WIDTH = 800
HEIGHT = 900
TOOLBAR_HEIGHT = HEIGHT - WIDTH

ROWS = COLS = 28

PIXEL_SIZE = WIDTH // ROWS

BACKGROUND_COLOR = WHITE
DRAW_COLOR = BLACK

DRAW_GRID_LINES = False

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guesser")


def get_font(size):
    return pygame.font.SysFont("comicsans", size)


def draw(win):
    win.fill(BACKGROUND_COLOR)
    pygame.display.update()


def create_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)


def draw_grid(win):
    for i in range(ROWS + 1):
        pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
    for i in range(COLS + 1):
        pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))



def main():
    clock = pygame.time.Clock()
    run = True
    mouse_down = False

    draw(WIN)
    grid = create_grid(ROWS, COLS, WHITE)
    draw_grid(WIN)
    pygame.display.update()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_down = True
            elif event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False

            if mouse_down:
                x, y = pygame.mouse.get_pos()
                row = x // PIXEL_SIZE
                col = y // PIXEL_SIZE

                if row < ROWS:
                    grid[row][col] = DRAW_COLOR

                pygame.draw.circle(WIN, BLACK, (x, y), 5)
                pygame.display.update()

    pygame.quit()


pygame.init()

if __name__ == "__main__":
    main()
