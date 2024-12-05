# Документация: python -m pygame.docs

import pygame

if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    # Смена кадров (обновление экрана)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
