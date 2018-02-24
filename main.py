
from __future__ import print_function
from __future__ import division
from Game import Snake, Segment, Food, get_index
import pygame
import time
colors = {'white': (255,255,255), 'black': (0,0,0), 'red':(255,0,0),
          'green': (0,255,0), 'blue': (0,0,255)}

def main():
    scr_width=600
    scr_height=600
    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont(None, 30)
    screen = pygame.display.set_mode([scr_width,scr_height])
    pygame.display.set_caption('snakes')
    done = False
    snake = Snake(color=colors['blue'], seg_color=colors['green'], size=(20, 20),
                  speed=2, width=scr_width, height=scr_height)
    food = Food(color=colors['red'], size=(10, 10), width=scr_width, height=scr_height)
    all_sprites = pygame.sprite.Group()
    all_sprites.add(snake)
    all_sprites.add(food)
    snake_body = pygame.sprite.Group()
    delay = 0.003
    while not done:
        key_pressed = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                done = True
            elif event.type == pygame.KEYDOWN:
                key_pressed = event.key
        screen.fill(colors['white'])
        eaten = pygame.sprite.collide_rect(snake, food)
        snake_body.draw(screen)
        all_sprites.draw(screen)
        sorted_segments = sorted(snake_body.sprites(),key=get_index)
        if eaten:
            if len(snake_body) == 0:
                snake_body.add(Segment(seg_color=colors['green'], size=(20, 20), pos=(snake.rect.x, snake.rect.y),
                                    number=len(snake_body), direction=snake.dir, distance=30))
            else:
                snake_body.add(Segment(seg_color=colors['green'], size=(20, 20),
                                       pos=(sorted_segments[-1].rect.x, sorted_segments[-1].rect.y),
                                       number=len(snake_body), direction=snake.dir, distance=30))
        snake_body.update(snake, sorted_segments)
        all_sprites.update(key_pressed, eaten)
        score = snake.get_score()
        textsurface = myfont.render('score: {}, segments: {}'.format(score, len(all_sprites)-2), True, colors['black'])
        screen.blit(textsurface, (0, scr_height-20))
        pygame.display.flip()
        time.sleep(delay)
    # for s in sorted_segments:
    #     print(s.rect)
    return


if __name__ == '__main__':
    main()




