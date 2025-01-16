import pygame
import random
from data.config import *



class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, colums, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheets(sheet, colums, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheets(self, sheet, colums, rows):
        self.rect = pygame.Rect(0,
                                0,
                                sheet.get_width() // colums,
                                sheet.get_height() // rows)
        for i in range(rows):
            for j in range(colums):
                frame_location = (self.rect.w * j, self.rect.h * i)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]

class Particle(pygame.sprite.Sprite):
    def __init__(self, fire, pos, dx, dy):
        super().__init__(all_sprites)
        for scale in (5, 10, 20):
            fire.append(pygame.transform.scale(fire[0], (scale, scale)))
        self.image = random.choice(fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()