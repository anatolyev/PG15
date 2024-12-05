# Документация: python -m pygame.docs
import random
import pygame


def draw(screen):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Pygame!",
                       True,
                       (100, 255, 100))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0),
                (text_x - 10, text_y - 10,
                 text_w + 20, text_h + 20), 1)


def draw2(screen):
    for i in range(1000):
        screen.fill(pygame.Color('white'),
                    (random.random() * width,
                     random.random() * height, 10, 2))


def draw3(screen):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0),
                     (100, 100,
                      200, 200), 1)
    pygame.draw.polygon(screen, pygame.Color('orange'), [(0, 0), (150, 50), (50, 150)], 0)


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    draw3(screen)
    # Смена кадров (обновление экрана)
    pygame.display.flip()

    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

