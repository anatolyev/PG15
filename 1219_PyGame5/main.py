# Example file showing a basic pygame "game loop"
import os
import sys
import pygame
from random import randrange


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

class Bomb(pygame.sprite.Sprite):

    def __init__(self, group, width, height):
        super().__init__(group)
        self.image = load_image("bomb.png")
        self.image_boom = load_image("boom.png")
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width)
        self.rect.y = randrange(height)

    def update(self, *args):
        self.rect = self.rect.move(randrange(3) - 1,
                                   randrange(3) - 1)
        if (args and args[0].type == pygame.MOUSEBUTTONDOWN and
                self.rect.collidepoint(args[0].pos)):
            self.image = self.image_boom



def main():
    # pygame setup
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)
    all_sprites = pygame.sprite.Group()
    for _ in range(50):
        Bomb(all_sprites, width, height)
    clock = pygame.time.Clock()
    # fill the screen with a color to wipe away anything from last frame
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)
        # RENDER YOUR GAME HERE
        screen.fill("purple")
        all_sprites.draw(screen)
        all_sprites.update()

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


if __name__ == '__main__':
    main()
