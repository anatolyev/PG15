import pygame
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

