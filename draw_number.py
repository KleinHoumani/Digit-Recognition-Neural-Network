import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 240

WIDTH = 700
HEIGHT = 850
TOOLBAR_HEIGHT = HEIGHT - WIDTH

ROWS = COLS = 28

PIXEL_SIZE = WIDTH // ROWS

BACKGROUND_COLOR = WHITE
DRAW_COLOR = BLACK

DRAW_GRID_LINES = False

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Neural Network")


class Button:
    def __init__(self, x, y, width, height, text, color, text_color, outline_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.outline_color = outline_color

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(win, self.outline_color, (self.x, self.y, self.width, self.height), 2)  # draw outline of button

        button_font = get_font(22)
        text_surface = button_font.render(self.text, True, self.text_color)
        win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, self.y + self.height / 2 - text_surface.get_height() / 2))

    def clicked(self, pos):
        x, y = pos

        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        else:
            return False




def get_font(size):
    return pygame.font.SysFont("comicsans", size)


def create_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    row = 0
    while row < len(grid):
        col = 0
        while col < len(grid[row]):
            pygame.draw.rect(win, grid[row][col], (row * PIXEL_SIZE, col * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
            col += 1
        row += 1

    for i in range(ROWS + 1):
        pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
    for i in range(COLS + 1):
        pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw(win, grid, buttons):
    win.fill(BACKGROUND_COLOR)

    draw_grid(WIN, grid)

    for button in buttons:
        button.draw(win)

    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    mouse_down = False

    grid = create_grid(ROWS, COLS, (150, 0, 150))
    draw_grid(WIN, grid)
    pygame.display.update()

    button_dimension = TOOLBAR_HEIGHT * 0.75
    button_y = HEIGHT - TOOLBAR_HEIGHT + (TOOLBAR_HEIGHT - button_dimension) / 2
    buttons = [
        Button(WIDTH // 10, button_y, button_dimension, button_dimension, "Clear", WHITE, BLACK, BLACK),
        Button(3 * WIDTH // 10, button_y, button_dimension, button_dimension, "Predict", WHITE, BLACK, BLACK)
    ]

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

                print(row, col)

                if row < ROWS and col < COLS:
                    grid[row][col] = DRAW_COLOR

        draw(WIN, grid, buttons)

    pygame.quit()


pygame.init()

if __name__ == "__main__":
    main()
