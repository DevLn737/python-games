import pygame
from paddle import Paddle
from ball import Ball
from score import Score
import os

# ----------------    INIT   ----------------

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.font.init()
pygame.display.set_caption('Pong game')
clock = pygame.time.Clock()

if not pygame.font.get_init():
    print("Error loading font")

fps_font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "Subway.ttf"), 14)
font = pygame.font.Font(os.path.join(os.path.dirname(__file__), "Subway.ttf"), 42)

running = True

# ----------------    GAME OBJECTS   ----------------
player = Paddle(
    screen,
    x=screen.get_width() - 25 - 25,
    y=screen.get_height() / 2 - 120 / 2,
    width=25,
    height=120,
)
enemy = Paddle(
    screen,
    x=25,
    y=screen.get_height() / 2 - 120 / 2,
    width=25,
    height=120,
    speed=3
)
ball = Ball(screen, screen.get_width() / 2, screen.get_height() / 2, 15, 5)
score = Score()


def draw_center_line():
    pygame.draw.line(
        screen,
        pygame.color.Color("white"),
        (screen.get_width() / 2, 0),
        (screen.get_width() / 2, screen.get_height()),
        width=1
    )


# ----------------    GAME LOOP   ----------------
while running:
    # EVENT HANDLE
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    keys = pygame.key.get_pressed()

    # UPDATE
    player.update(keys)
    enemy.ai_update(ball.y)
    ball.update(player=player, enemy=enemy, score=score)

    # DRAW
    screen.fill("Black")

    draw_center_line()

    score.draw(screen, font)
    player.draw()
    enemy.draw()
    ball.draw()

    # Отображение FPS
    fps_text = fps_font.render(str(round(clock.get_fps(), 2)), True, pygame.color.Color('gray'))
    screen.blit(fps_text, (5, 5))

    # Обновляем экран
    pygame.display.flip()

    clock.tick(60)
