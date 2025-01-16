# Общие зависимости:
import os
import sys
import pygame
import random

# Внутренние зависимости:
from data.config import *
from data.classes import *


def load_image(name, color_key=None):
    """Загрузка изображений"""
    fullname = os.path.join(IMAGES, name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Невозможно загрузить изображение из файла:', fullname)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image

def terminate():
    """Выход из игры"""
    pygame.quit()
    sys.exit()


def create_particles(position):
    fire = [load_image("star.png")]
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    global set_particles
    for _ in range(particle_count):
        set_particles.append(Particle(fire, position,
                                      random.choice(numbers),
                                      random.choice(numbers)))
    for part in set_particles:
        if abs(part.rect.x) > WIDTH or abs(part.rect.y) > HEIGHT:
            set_particles.remove(part)
        print(len(set_particles))

def game_cycle():
    """Главный игровой цикл"""
    dragon = AnimatedSprite(load_image("dragon_sheet8x2.png"), 8, 2, 50, 50)
    sound = pygame.mixer.Sound(SOUNDS + "vineboom.mp3")
    vol = 1
    running = True
    сount_animation = 0
    global set_particles
    set_particles = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                create_particles(pygame.mouse.get_pos())
                channel = sound.play()
                sound.set_volume(vol)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                vol += 0.1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                vol -= 0.1
            sound.set_volume(vol)
        screen.fill(pygame.Color(0, 0, 0))
        if сount_animation % 5 == 0:
            # all_sprites.update()
            dragon.update()
            сount_animation = 0
        сount_animation += 1
        for fire in set_particles:
            fire.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    terminate()

