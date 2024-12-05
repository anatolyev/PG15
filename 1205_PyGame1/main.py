# Документация: python -m pygame.docs

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
                 text_w + 10, text_h + 10))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    draw(screen)
    # Смена кадров (обновление экрана)
    pygame.display.flip()



    while pygame.event.wait().type != pygame.QUIT:
        pass

    pygame.quit()

