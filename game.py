import pygame
from player import Player
from monster import Monster


# Créer la Classe du jeu
class Game:
    def __init__(self):
        # Generer joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de Monstres
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
        self.isPlaying = False

    def start(self):
        self.isPlaying = True
        self.spawn_monster()

    def game_over(self):
        # Reinit le jeu
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.isPlaying = False

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        # Appliquer barre de vie du joueur
        self.player.update_health_bar(screen)
        
        # Recuperer projectile
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        # Récupérer les Monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # Dessiner Image projectiles
        self.player.all_projectiles.draw(screen)
        
        # Dessiner Groupe de monstre
        self.all_monsters.draw(screen)
        
        # Vérifier si à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()



    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
