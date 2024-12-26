import pygame


class Paddle:
    def __init__(
            self,
            screen: pygame.Surface,
            x: float,
            y: float,
            width: int,
            height: int,
            speed: float = 7,
            acceleration: float = 1.5,
    ):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.acceleration = acceleration

    def update(self, keys):
        current_speed = (
            self.speed * self.acceleration if keys[pygame.K_LSHIFT] else self.speed
        )

        if keys[pygame.K_w] and self.y > 0:
            self.y -= current_speed
        elif keys[pygame.K_s] and self.y + self.height < self.screen.get_height():
            self.y += current_speed

    def ai_update(self, ball_y):
        paddle_center = self.y + self.height / 2

        if paddle_center != ball_y:
            if ball_y > paddle_center:
                self.y += self.speed
            elif ball_y < paddle_center:
                self.y -= self.speed

    def draw(self):
        pygame.draw.rect(
            self.screen,
            pygame.color.Color("WHITE"),
            pygame.Rect(self.x, self.y, self.width, self.height),
        )
