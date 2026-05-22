import pygame
import random

pygame.init()

width = 600
height = 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 35)

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [200, 180])

def gameLoop():

    game_over = False

    x = 300
    y = 200

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -10
                    y_change = 0

                elif event.key == pygame.K_RIGHT:
                    x_change = 10
                    y_change = 0

                elif event.key == pygame.K_UP:
                    y_change = -10
                    x_change = 0

                elif event.key == pygame.K_DOWN:
                    y_change = 10
                    x_change = 0

        x += x_change
        y += y_change

        screen.fill(black)

        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        for block in snake_list:
            pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()

gameLoop()