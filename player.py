import pygame
from projectile import Projectile
#import random
import animation


# Créer la Classe joueur
class Player(animation.AnimateSprite): #pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        #self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
        self.start_animation()
        self.game.soundManager.play('tir')

    def move_right(self):
        # Si le joueur n'est pas en collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def update_health_bar(self, surface):
        # bar de vie du joueur
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (111,210,46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])

    def damage(self, amount):
        # Dégats subis du joueur
        if self.health - amount > amount:
            self.health -= amount # infliger dégats
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()
