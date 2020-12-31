import pygame
from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent

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
        # Comet
        self.comet_event = CometFallEvent(self)

    def start(self):
        self.isPlaying = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def game_over(self):
        # Reinit le jeu
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.isPlaying = False
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        # Actualiser la barre d'événement du jeu
        self.comet_event.update_bar(screen)
        # Actualiser l'animation du joueur
        self.player.update_animation()

        # Recuperer projectile
        for projectile in self.player.all_projectiles:
            projectile.move()
        
        # Récupérer les Monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # Récupérer les comètes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # Dessiner Image projectiles
        self.player.all_projectiles.draw(screen)
        
        # Dessiner Groupe de monstre
        self.all_monsters.draw(screen)

        # Appliquer les comètes
        self.comet_event.all_comets.draw(screen)
        
        # Vérifier si à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monsterClassName):
        #monster = Mummy(self)
        self.all_monsters.add(monsterClassName.__call__(self))
