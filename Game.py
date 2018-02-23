

from __future__ import print_function
from __future__ import division
import pygame
from random import randint

class Snake(pygame.sprite.Sprite):
    # directions = ['l', 'r', 'u', 'd']
    def __init__(self, color, size, length=3, width=600, height=600):
        super(Snake,self).__init__()
        self.image = pygame.Surface([size[0],size[1]])
        self.image.fill(color=color)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.dir = 'l'
        self.w = width
        self.h = height
        return

    def this_key(self, key):
        self.key = key
        # print(self.key)

    def update(self, *args):
        # print(self.key)
        if self.key:
            if self.key == 273:
                self.dir = 'u'
            elif self.key == 275:
                self.dir = 'r'
            elif self.key == 274:
                self.dir = 'd'
            elif self.key == 276:
                self.dir = 'l'

        if self.dir == 'r':
            self.rect.x += 1
        elif self.dir == 'l':
            self.rect.x -= 1
        elif self.dir == 'u':
            self.rect.y -= 1
        elif self.dir == 'd':
            self.rect.y += 1

        if self.rect.x > self.w:
            self.rect.x = 0
        elif self.rect.y > self.h:
            self.rect.y = 0
        elif self.rect.x < 0:
            self.rect.x = self.w-1
        elif self.rect.y < 0:
            self.rect.y = self.h-1

        print(self.rect.x, self.rect.y)
        pass


class Food(pygame.sprite.Sprite):
    def __init__(self, color, size, width=600, height=600):
        super(Food, self).__init__()
        self.image = pygame.Surface([size[0], size[1]])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.w = width
        self.h = height
        self.rect.x = randint(0,self.w)
        self.rect.y = randint(0,self.h)
        self.score = 0
        return

    def this_status(self, status):
        self.status = status

    def update(self, *args):
        if self.status == 1:
            self.score += 1
            print(self.score)
            self.rect.x = randint(0, self.w)
            self.rect.y = randint(0, self.h)
        return







