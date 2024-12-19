# Example file showing a basic pygame "game loop"
import os
import sys
import pygame

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

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")
    image = load_image('robot.png', -1)
    image1 = pygame.transform.scale(image, (300, 100))
    screen.blit(image1, (100, 200))
    image2 = pygame.transform.scale(image, (100, 300))
    screen.blit(image2, (400, 200))
    image3 = pygame.transform.scale(image, (200, 50))
    screen.blit(image3, (700, 200))
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.blit(image, event.pos)
        # RENDER YOUR GAME HERE
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


if __name__ == '__main__':
    main()
