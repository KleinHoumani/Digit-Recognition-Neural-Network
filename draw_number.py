import pygame
import tensorflow as tf
import numpy as np


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

        button_font = get_font(26)
        text_surface = button_font.render(self.text, True, self.text_color)
        win.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, self.y + self.height / 2 - text_surface.get_height() / 2))

    def clicked(self, x, y):
        if self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height:
            return True
        else:
            return False


def get_font(size):
    return pygame.font.SysFont("calibri", size)


def create_grid(rows, cols, color):
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(color)

    return grid


def draw_grid(win, grid):
    for row in range(ROWS):
        for col in range(COLS):
            pygame.draw.rect(win, grid[row][col], (col * PIXEL_SIZE, row * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))

    for i in range(ROWS + 1):
        pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
    for i in range(COLS + 1):
        pygame.draw.line(win, BLACK, (i * PIXEL_SIZE, 0), (i * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))


def draw_prediction(win, prediction_num):
    prediction_text = "Prediction:"
    prediction_font = get_font(36)
    num_font = get_font(60)
    text_surface = prediction_font.render(prediction_text, True, BLACK)
    num_surface = num_font.render(prediction_num, True, BLACK)
    win.blit(text_surface, (6 * WIDTH // 10, HEIGHT - TOOLBAR_HEIGHT // 1.75 - text_surface.get_height()))
    win.blit(num_surface, (6 * WIDTH // 10 + text_surface.get_width() // 2 - num_surface.get_width() + 10, HEIGHT - TOOLBAR_HEIGHT // 2 + text_surface.get_height() // 2 - num_surface.get_height() + 30))


def draw(win, grid, buttons, prediction_num):
    win.fill(BACKGROUND_COLOR)

    draw_grid(WIN, grid)

    for button in buttons:
        button.draw(win)

    draw_prediction(WIN, prediction_num)

    pygame.display.update()


def convert_to_binary(rows, cols, grid):
    new_grid = []

    for row in range(rows):
        new_grid.append([])
        for col in range(cols):
            if grid[row][col] == (0, 0, 0):
                new_grid[row].append(1)
            else:
                new_grid[row].append(0)

    return new_grid


def main():
    clock = pygame.time.Clock()
    run = True

    mouse_down = False
    model = tf.keras.models.load_model('num_reader')
    prediction_num = ""
    grid = create_grid(ROWS, COLS, WHITE)
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
                row = y // PIXEL_SIZE
                col = x // PIXEL_SIZE

                if row < ROWS and col < COLS:
                    grid[row][col] = DRAW_COLOR
                else:
                    for button in buttons:
                        if button.clicked(x, y):
                            if button.text == 'Clear':
                                grid = create_grid(ROWS, COLS, WHITE)
                            if button.text == 'Predict':
                                binary_grid = np.array(convert_to_binary(ROWS, COLS, grid))
                                prediction = np.argmax(model.predict([binary_grid.reshape(1, 28, 28)]))
                                prediction_num = str(prediction)

        draw(WIN, grid, buttons, prediction_num)

    pygame.quit()


pygame.init()

if __name__ == "__main__":
    main()
