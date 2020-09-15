import pygame
import random

# Créer Monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def forward(self):
        # Deplacement si pas collision avec groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # Colision monstre avec joueur pour infliger dégats
        else:
            self.game.player.damage(self.attack)

    def update_health_bar(self, surface):
        # bar de vie du monstre
        bar_color = (111,210,46)
        back_bar_color = (60,63,60)
        bar_position = [self.rect.x + 10, self.rect.y - 10, self.health, 5]
        back_bar_position = [self.rect.x + 10, self.rect.y - 10, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def damage(self, amount):
         # Dégats subis du monstre
        self.health -= amount # infliger dégats
        if self.health <= 0: # respawn
            self.health = self.max_health
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
        
        if self.game.comet_event.is_full_loaded():
            self.game.all_monsters.remove(self)
            # Appel pluie de comètes
            self.game.comet_event.attempt_fall()
