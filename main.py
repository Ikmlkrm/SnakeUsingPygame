from operator import truediv

import pygame
import logging
import sys
import random
from pygame.math import Vector2

# Set up the logging configuration
logging.basicConfig(
    filename='app_log.txt',  # Log file where logs will be saved
    level=logging.INFO,      # Log level (INFO, DEBUG, ERROR, etc.)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format
)

class Snake:
    def __init__(self):

        self.head = None
        self.tail = None

        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(1,0)
        self.new_block = False

        self.head_up = pygame.image.load('Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('Graphics/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('Graphics/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('Graphics/head_right.png').convert_alpha()

        self.tail_up = pygame.image.load('Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('Graphics/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('Graphics/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('Graphics/tail_right.png').convert_alpha()

        self.body_vertical = pygame.image.load('Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load('Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load('Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load('Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('Graphics/body_bl.png').convert_alpha()

        self.munch_sound = pygame.mixer.Sound('Sounds/Munch.mp3')
        self.game_over_sound = pygame.mixer.Sound('Sounds/RetroGameOver.mp3')

        # logging.info(f"1. game_over_played_value: {self.game_over_played}")



    def draw_snake(self):

        self.update_head_graphics()
        self.update_tail_graphics()


        for index, block in enumerate(self.body):
            # 1. Need rectangle for graphics position
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size)
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            # 2. Direction face is heading
            if index == 0:
                screen.blit(self.head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block

                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)

                elif previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)

                else:
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0):
            self.head = self.head_left

        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right

        elif head_relation == Vector2(0, 1):
            self.head = self.head_up

        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left

        elif tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right

        elif tail_relation == Vector2(0, 1):
            self.tail = self.tail_up

        elif tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):
        if self.new_block:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

            self.new_block = False

        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        self.new_block = True

    def play_munch_sound(self):
        self.munch_sound.play()

    def play_game_over(self):
            self.game_over_sound.play()



    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)

    def start_game(self):


        game_over_text = str("SNAKE")
        game_over_surface = game_over_font.render(game_over_text, True, (0, 0, 0))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.center = (cell_size * cell_number // 2, 150)
        screen.blit(game_over_surface, game_over_rect)

        continue_game_text = "Press WASD to start"
        continue_game_surface = continue_game_font.render(continue_game_text, True, (0, 0, 0))
        continue_game_rect = continue_game_surface.get_rect()
        continue_game_rect.center = (cell_size * cell_number // 2, 250)
        screen.blit(continue_game_surface, continue_game_rect)




    def game_over_screen(self):
        if self.direction == Vector2(0,0):

            game_over_text = str("GAME OVER")
            game_over_surface = game_over_font.render(game_over_text, True, (0,0,0))
            game_over_rect = game_over_surface.get_rect()
            game_over_rect.center = (cell_size * cell_number // 2, 150)
            screen.blit(game_over_surface, game_over_rect)

            continue_game_text = "Press WASD to continue playing"
            continue_game_surface = continue_game_font.render(continue_game_text, True, (0, 0, 0))
            continue_game_rect = continue_game_surface.get_rect()
            continue_game_rect.center = (cell_size * cell_number // 2, 250)
            screen.blit(continue_game_surface, continue_game_rect)


class Fruit:
    def __init__(self):
        # Create an x and y position
        # Draw a square

        self.pos = None
        self.x = None
        self.y = None

        self.randomize()

    def draw_fruit(self):
        # create rectangle
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size), cell_size, cell_size)

        # draw fruit
        screen.blit(apple, fruit_rect)
        # pygame.draw.rect(screen,(126, 166, 114),fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)

        self.pos = Vector2(self.x, self.y)

class Main:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.high_score = 0
        self.game_start = False

        self.game_over_flag = False
        logging.info(f"1. game over flag value: {self.game_over_flag}")

    def update(self):
        if self.game_start:
            self.snake.move_snake()
            self.check_collision()
            self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
        self.draw_high_score()

        if not self.game_start:
            self.snake.start_game()

        if self.game_start:
            self.snake.game_over_screen()


    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:

            self.fruit.randomize()

            self.snake.add_block()

            self.snake.play_munch_sound()

            for block in self.snake.body[1:]:
                if block == self.fruit.pos:
                    self.fruit.randomize()

    def check_fail(self):
        # checks if snake it outside of screen
        if not -1 <= self.snake.body[0].x <= cell_number:
            self.game_over()

        if not -1 <= self.snake.body[0].y <= cell_number:
            self.game_over()

        # checks if snake is eating itself
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):

        logging.info(f"Check game over flag value: {self.game_over_flag}")
        if not self.game_over_flag:
            self.snake.play_game_over()
            self.game_over_flag = True
            logging.info(f"2. game over flag value: {self.game_over_flag}")

        self.snake.reset()

    def draw_grass(self):
        grass_color = (242,210,169)

        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col*cell_size , row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col*cell_size , row*cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):
        score_text = str((len(self.snake.body) - 3))
        score_surface = game_font.render(score_text,True,(1, 70, 1))
        score_x = int(cell_size*cell_number-720)
        score_y = int(cell_size*cell_number-40)
        score_rect = score_surface.get_rect(center = (score_x, score_y))


        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))

        bg_rect = pygame.Rect(apple_rect.left - 5, apple_rect.top - 2,(apple_rect.width + score_rect.width + 10), apple_rect.height +4)

        pygame.draw.rect(screen, (225,191,146), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (0,0,0), bg_rect,2)

    def draw_high_score(self):
        score_text = len(self.snake.body) - 3

        if score_text > self.high_score:
            self.high_score = score_text

        high_score_text = str(f"HI:{self.high_score}")

        score_surface = high_score_font.render(high_score_text,True,(1, 70, 1))
        score_x = int(cell_size*cell_number-60)
        score_y = int(cell_size*cell_number-30)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        bg_rect = pygame.Rect(score_rect.left - 5, score_rect.top -4, score_rect.width+10, score_rect.height+6)

        pygame.draw.rect(screen, (225,191,146), bg_rect)
        screen.blit(score_surface, score_rect)
        pygame.draw.rect(screen, (0,0,0), bg_rect,2)


class Start:
    def __init__ (self):
        # Create the start screen
        #

        pass


pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

cell_size = 40
cell_number = 20

SCREEN_WIDTH = cell_size*cell_number
SCREEN_HEIGHT = cell_size*cell_number

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

apple = pygame.image.load('Graphics/watermelon.png')

game_font = pygame.font.Font('Graphics/game_font_2.ttf', 30)
game_over_font = pygame.font.Font('Graphics/robust.ttf', 150)
continue_game_font = pygame.font.Font('Graphics/robust.ttf', 50)
high_score_font = pygame.font.Font('Graphics/game_font_2.TTF', 30)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

start_game = Start()
main_game = Main()


while True:
    # Where you draw all elements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    main_game.game_over_flag = False
                    main_game.game_start = True
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)

                if event.key == pygame.K_s:
                    main_game.game_over_flag = False
                    main_game.game_start = True
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)

                if event.key == pygame.K_d:
                    main_game.game_over_flag = False
                    main_game.game_start = True
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)

                if event.key == pygame.K_a:
                    main_game.game_over_flag = False
                    main_game.game_start = True
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)

    screen.fill((246,215,176))

    main_game.draw_elements()

    pygame.display.update()
    clock.tick(120)