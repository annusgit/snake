
from __future__ import print_function
from __future__ import division
from Game import Snake, Food
import pygame
import time


colors = {'white': (255,255,255), 'black': (0,0,0), 'red':(255,0,0),
          'green': (0,255,0), 'blue': (0,0,255)}

def main():
    scr_width=600
    scr_height=600
    pygame.init()
    screen = pygame.display.set_mode([scr_width,scr_height])
    done = False
    snake = Snake(color=colors['blue'], size=(10, 10), width=scr_width, height=scr_height)
    food = Food(color=colors['red'], size=(10, 10), width=scr_width, height=scr_height)
    sprites = pygame.sprite.Group()
    sprites.add(snake)
    # sprites.add(food)
    delay=0.003
    while not done:
        key = None
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                key = key.index(1)
        screen.fill(colors['white'])
        hit = pygame.sprite.spritecollide(snake, sprites, True)
        # print(hit)
        snake.this_key(key)
        # food.this_status(hit)
        sprites.draw(screen)
        sprites.update()
        pygame.display.flip()
        time.sleep(delay)
    return


if __name__ == '__main__':
    main()




