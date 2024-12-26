import pygame


class Ball:
    def __init__(
            self,
            screen: pygame.Surface,
            x: float,
            y: float,
            radius: float,
            speed_x: float = 5,
            speed_y: float = 5,
    ):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, player, enemy, score):
        # Проверка столкновения с ракеткой
        if self._check_paddle_collision(player) or self._check_paddle_collision(enemy):
            # Опционально усложнение (Ускоряем мяч на 1% при каждом столкновении)
            # self.speed_x *= -1.01
            # self.speed_y *= 1.01
            self.speed_x *= -1

        # Проверка столкновения со стеной
        self._check_wall_collision(score)

        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self):
        pygame.draw.circle(
            self.screen,
            pygame.color.Color("WHITE"),
            (self.x, self.y), self.radius
        )

    def _reset_position(self):
        """Сброс позиции мяча на центр экрана."""
        self.x = self.screen.get_width() // 2
        self.y = self.screen.get_height() // 2
        self.speed_x = 5
        self.speed_y = 5

    def _check_wall_collision(self, score):
        if self.y - self.radius <= 0 or self.y + self.radius >= self.screen.get_height():
            self.speed_y *= -1

        # Вышел за правую стену
        if self.x + self.radius >= self.screen.get_width():
            score.increase_player_score()
            self._reset_position()

        # Вышел за левую стену
        if self.x - self.radius <= 0:
            score.increase_enemy_score()
            self._reset_position()

        # if self.x - self.radius <= 0 or self.x + self.radius >= self.screen.get_width():
        #     self.speed_x *= -1

    def _check_paddle_collision(self, paddle):
        ball_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
        paddle_rect = pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.height)

        return ball_rect.colliderect(paddle_rect)

