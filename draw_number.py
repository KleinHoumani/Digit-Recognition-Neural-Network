import pygame

black = (0, 0, 0)
grey = (200, 200, 215)
# class pixel(object):
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.color = (255, 255, 255)
#         self.neighbors = []
#
#     def draw(self, surface):


width, height = 900, 500
size = [width, height]

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Number Guesser")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()


pygame.init()

if __name__ == "__main__":
    main()
