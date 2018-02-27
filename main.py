
from __future__ import print_function
from __future__ import division
from Game import Snake, Segments, Food
import pygame
import time

colors = {'white': (255,255,255), 'black': (0,0,0), 'red':(255,0,0),
          'green': (0,255,0), 'blue': (0,0,255)}

def get_color(x):
   if x % 2 == 0:
       return colors['black']
   else:
       return colors['green']

def main():
    scr_width = 600
    scr_height = 600
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont(None, 30)
    screen = pygame.display.set_mode([scr_width,scr_height])
    pygame.display.set_caption('snakes')
    done = False
    snake_size = 15
    food_size = 8
    initial_length = 3
    snake = Snake(color=colors['black'], size=(snake_size, snake_size), speed=snake_size,
                  width=scr_width, height=scr_height)
    food = Food(color=colors['red'], size=(food_size,food_size), width=scr_width, height=scr_height)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(snake)
    all_sprites.add(food)
    snake_body = Segments()
    for _ in range(initial_length):
        snake_body.add_seg(head_pos=(snake.rect.x, snake.rect.y), size=(snake_size, snake_size),
                           color=get_color(len(snake_body.list)))
    delay = 0.05
    while not done:
        key_pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                done = True
            elif event.type == pygame.KEYDOWN:
                key_pressed = event.key
        screen.fill(colors['white'])
        eaten = pygame.sprite.collide_rect(snake, food)
        if eaten:
            snake_body.add_seg(head_pos=(snake.rect.x, snake.rect.y), size=(snake_size, snake_size),
                               color=get_color(len(snake_body.list)))
        snake_body.update((snake.rect.x, snake.rect.y))
        all_sprites.update(key_pressed, eaten)
        score = snake.get_score()
        textsurface = myfont.render('score: {}'.format(score), True, colors['black'])
        screen.blit(textsurface, (0, scr_height-20))
        all_sprites.draw(screen)
        snake_body.draw(screen)
        pygame.display.flip()
        time.sleep(delay)
    return


if __name__ == '__main__':
    main()




