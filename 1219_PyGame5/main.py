# Example file showing a basic pygame "game loop"
import os
import sys
import pygame

def load_image(name):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением "{fullname}" не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    image = load_image('')
    running = True

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # RENDER YOUR GAME HERE
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(60)  # limits FPS to 60
    pygame.quit()


if __name__ == '__main__':
    main()
