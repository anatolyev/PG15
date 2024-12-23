# Example file showing a basic pygame "game loop"
import os
import sys
import pygame
import random

ALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_BORDERS = pygame.sprite.Group()
VERTICAL_BORDERS = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()  # оптимизирует формат изображения и ускоряет отрисовку
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()  # спользуется для добавления прозрачности к изображению
    return image



class Mountain(pygame.sprite.Sprite):
    image = load_image("mountains.png", -1)

    def __init__(self, size):
        super().__init__(ALL_SPRITES)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = size[0]


class Landing(pygame.sprite.Sprite):
    image = load_image("pt.png", -1)

    def __init__(self, pos):
        super().__init__(ALL_SPRITES)
        self.image = Landing.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def update(self):
        self.rect = self.rect.move(0, 1)


def main():
    # pygame setup
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    mountain = Mountain(size)

    clock = pygame.time.Clock()
    # fill the screen with a color to wipe away anything from last frame

    # images = load_image('bomb.png')
    running = True

    while running:

        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Landing(event.pos)
        # RENDER YOUR GAME HERE
        screen.fill(pygame.Color("black"))
        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


if __name__ == '__main__':
    main()
