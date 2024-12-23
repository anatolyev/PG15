# Example file showing a basic pygame "game loop"
import os
import sys
import pygame
import random

ALL_SPRITES = pygame.sprite.Group()
HORIZONTAL_BORDERS = pygame.sprite.Group()
VERTICAL_BORDERS = pygame.sprite.Group()


# def load_image(name):
#     fullname = os.path.join('images', name)
#     if not os.path.isfile(fullname):
#         print(f'Файл с изображением "{fullname}" не найден')
#         sys.exit()
#     images = pygame.images.load(fullname)
#     return images

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y):
        super().__init__(ALL_SPRITES)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-5, 5)
        self.vy = random.randrange(-5, 5)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, HORIZONTAL_BORDERS):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, VERTICAL_BORDERS):
            self.vx = -self.vx



class Border(pygame.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(ALL_SPRITES)
        if x1 == x2:  # вертикальная стенка
            self.add(VERTICAL_BORDERS)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(HORIZONTAL_BORDERS)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)



def main():
    # pygame setup
    pygame.init()
    size = width, height = 1280, 720
    screen = pygame.display.set_mode(size)

    Border(5, 5, width - 5, 5)
    Border(5, height - 5, width - 5, height - 5)
    Border(5, 5, 5, height - 5)
    Border(width - 5, 5, width - 5, height - 5)

    for i in range(10):
        Ball(20, 100, 100)


    clock = pygame.time.Clock()
    # fill the screen with a color to wipe away anything from last frame

    # images = load_image('bomb.png')
    running = True

    while running:
        screen.fill("white")
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     screen.blit(images, event.pos)
        # RENDER YOUR GAME HERE
        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update()

        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


if __name__ == '__main__':
    main()
