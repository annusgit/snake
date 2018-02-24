

from __future__ import print_function
from __future__ import division

from six.moves import xrange
import pygame
from random import randint

class Snake(pygame.sprite.Sprite):
    # directions = ['l', 'r', 'u', 'd']
    def __init__(self, color, seg_color, size, speed, length=3, width=600, height=600):
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
        self.seg_color = seg_color
        self.size = size
        self.score = 0
        return

    def update(self, *args):
        [key, eaten] = args
        if key:
            if key == 273:
                self.dir = 'u'
            elif key == 275:
                self.dir = 'r'
            elif key == 274:
                self.dir = 'd'
            elif key == 276:
                self.dir = 'l'
        if eaten:
            self.score += 1

        if self.dir == 'r':
            self.rect.x += self.speed*self.dt
        elif self.dir == 'l':
            self.rect.x -= self.speed*self.dt
        elif self.dir == 'u':
            self.rect.y -= self.speed*self.dt
        elif self.dir == 'd':
            self.rect.y += self.speed*self.dt

        if self.rect.x > self.w:
            self.rect.x = 0
        elif self.rect.y > self.h:
            self.rect.y = 0
        elif self.rect.x < 0:
            self.rect.x = self.w-1
        elif self.rect.y < 0:
            self.rect.y = self.h-1

    def get_score(self):
        return self.score


class Segment(pygame.sprite.Sprite):
    def __init__(self, seg_color, size, pos, number, direction, distance):
        super(Segment, self).__init__()
        self.image = pygame.Surface(size)
        self.image.fill(color=seg_color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.d = distance
        if direction == 'l':
            self.rect.x += self.d
        elif direction == 'r':
            self.rect.x -= self.d
        elif direction == 'u':
            self.rect.y += self.d
        else:
            self.rect.y -= self.d

        self.number = number
        return

    def update(self, *args):
        snake, sprites = args
        if self.number == 0:
            self.rect.x = snake.rect.x
            self.rect.y = snake.rect.y
            # print(self.rect, snake.rect)
        else:
            self.rect.x = sprites[self.number-1].rect.x
            self.rect.y = sprites[self.number-1].rect.y
            # print(self.rect, sprites[self.number-1].rect)
        return


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


def get_index(seg):
    return seg.number






