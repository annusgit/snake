

from __future__ import print_function
from __future__ import division

import pygame
from random import randint

class Snake(pygame.sprite.Sprite):
    def __init__(self, color, size, speed, width=600, height=600):
        super(Snake,self).__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color=color)
        self.rect = self.image.get_rect()
        self.rect.x = randint(20, width - 20)
        self.rect.y = randint(20, height - 20)
        self.speed = speed
        self.dt = 1
        self.dir = 'r'
        self.w = width
        self.h = height
        self.size = size
        self.score = 0
        self.opposite_direction = {'l':'r', 'r':'l', 'u':'d', 'd':'u'}
        self.keys_to_directions = {273:'u', 275:'r', 274:'d', 276:'l'}
        return

    def update(self, *args):
        [key, eaten] = args
        self.score += 1 if eaten else 0
        if key in self.keys_to_directions.keys():
            self.dir = self.keys_to_directions[key] if self.keys_to_directions[key] != self.opposite_direction[self.dir] \
                else self.dir
        if self.dir == 'r':
            self.rect.x += self.speed*self.dt
        elif self.dir == 'l':
            self.rect.x -= self.speed*self.dt
        elif self.dir == 'u':
            self.rect.y -= self.speed*self.dt
        elif self.dir == 'd':
            self.rect.y += self.speed*self.dt

        if self.rect.x > self.w:
            self.rect.x = 1
        elif self.rect.y > self.h:
            self.rect.y = 1
        elif self.rect.x < 0:
            self.rect.x = self.w-1
        elif self.rect.y < 0:
            self.rect.y = self.h-1

    def get_score(self):
        return self.score


class Segment(pygame.sprite.Sprite):
    def __init__(self, seg_color, size, pos, distance):
        super(Segment, self).__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color=seg_color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.d = distance


class Segments(object):

    def __init__(self):
        self.list = []

    def draw(self, screen):
        for seg in self.list:
            screen.blit(seg.image, seg.rect)

    def update(self, head_pos):
        if len(self.list) > 0:
            for i in range(len(self.list)-1, 0, -1):
                self.list[i].rect.x, self.list[i].rect.y = self.list[i-1].rect.x, self.list[i-1].rect.y
            self.list[0].rect.x, self.list[0].rect.y = head_pos

    def positions(self):
        for seg in self.list:
            print(seg.rect.x, seg.rect.y)

    def add_seg(self, head_pos, size, color):
        if not len(self.list):
            pos = (head_pos[0], head_pos[1])
        else:
            pos = (self.list[-1].rect.x, self.list[-1].rect.y)
        self.list.append(Segment(seg_color=color, size=size, pos=pos, distance=30))


class Food(pygame.sprite.Sprite):
    def __init__(self, color, size, width=600, height=600):
        super(Food, self).__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.w = width
        self.h = height
        self.rect.x = randint(0,self.w)
        self.rect.y = randint(0,self.h)
        self.score = 0
        return

    def update(self, *args):
        status = args[1]
        if status == 1:
            self.rect.x = randint(20, self.w-20)
            self.rect.y = randint(20, self.h-20)
        return






