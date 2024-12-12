import pygame

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size



def main():
    # pygame setup
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Клетка")
    board = Board(5, 7)
    running = True

    while running:

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        pygame.display.flip()
        # limits FPS to 60
        # independent physics.
        dt = clock.tick(30) / 1000

    pygame.quit()


if __name__ == '__main__':
    main()


