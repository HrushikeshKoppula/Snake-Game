import pygame
import sys
import random

pygame.init()
screen_size = (screen_width, screen_height) = (800, 600)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
tick_speed = 10
running = True
Lost = False

class Food:
    def __init__(self, color="red"):
        self.size = 20
        self.color = color
        self.x = random.randint(0, (screen_width - self.size) // self.size) * self.size
        self.y = random.randint(0, (screen_height - self.size) // self.size) * self.size

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

class Snake:
    def __init__(self):
        self.size = 20
        self.color = "black"
        self.speed = 20
        self.body = [(screen_width//2,screen_height//2)]
        self.direction = "RIGHT"

    def move(self):
        x, y = self.body[0]
        if self.direction == "UP":
            y -= self.speed
        elif self.direction == "DOWN":
            y += self.speed
        elif self.direction == "LEFT":
            x -= self.speed
        elif self.direction == "RIGHT":
            x += self.speed
        self.body.insert(0, (x, y))
        self.body.pop()

    def change_direction(self, keys):
        if keys[pygame.K_LEFT] and self.direction != "RIGHT":
            self.direction = "LEFT"
        elif keys[pygame.K_RIGHT] and self.direction != "LEFT":
            self.direction = "RIGHT"
        elif keys[pygame.K_UP] and self.direction != "DOWN":
            self.direction = "UP"
        elif keys[pygame.K_DOWN] and self.direction != "UP":
            self.direction = "DOWN"

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, self.color, (segment[0], segment[1], self.size, self.size))

    def check_collision(self):
        if (
            self.body[0][0] < 0
            or self.body[0][0] > screen_width - 20
            or self.body[0][1] < 0
            or self.body[0][1] > screen_height - 20
        ):
            return True
        for segment in self.body[1:]:
            if self.body[0] == segment:
                return True
        return False

food = Food()
snake = Snake()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    snake.change_direction(keys)
    snake.move()

    if snake.check_collision():
        # Lost = True
        pygame.quit()
        sys.exit()

    if snake.body[0] == (food.x, food.y):
        snake.body.insert(0, snake.body[0])
        food = Food()

    screen.fill("white")

    food.draw()
    snake.draw()

    pygame.display.flip()

    clock.tick(tick_speed)

pygame.quit()
sys.exit()
