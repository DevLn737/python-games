class Score:
    def __init__(self, player_score=0, enemy_score=0):
        self.player_score = player_score
        self.enemy_score = enemy_score

    def increase_player_score(self):
        self.player_score += 1

    def increase_enemy_score(self):
        self.enemy_score += 1

    def draw(self, screen, font):
        player_score_text = font.render(str(self.player_score), True, (255, 255, 255))
        enemy_score_text = font.render(str(self.enemy_score), True, (255, 255, 255))

        screen.blit(player_score_text,
                    (screen.get_width() / 2 - player_score_text.get_width() / 2 - screen.get_width() / 10,
                     screen.get_height() / 2 - player_score_text.get_height() / 2))
        screen.blit(enemy_score_text,
                    (screen.get_width() / 2 - enemy_score_text.get_width() / 2 + screen.get_width() / 10,
                     screen.get_height() / 2 - enemy_score_text.get_height() / 2))
