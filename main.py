import pygame
import math
from game import Game
pygame.init()


# Générer la fenêtre du jeu
pygame.display.set_caption("Comet fall Game HD")
screen = pygame.display.set_mode((1080, 720))

# Charger l'arrière-plan
background = pygame.image.load('assets/bg.jpg')
 
# Charger Baniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil( screen.get_width() / 4)

# Charger le bouton d'accueil
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil( screen.get_width() / 3.33)
play_button_rect.y = math.ceil( screen.get_height() / 2)

# Charger le jeu
game = Game()

running = True

while running:
    # Appliquer la fenêtre du jeu
    screen.blit(background, (0, -200))

    # Le jeu a t'il commencé?
    if game.isPlaying:
        game.update(screen)
    else:
        # Afficher ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # Mettre à jour l'écran
    pygame.display.flip()

    # Jeu en cours
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # Lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # souris sur bouton jouer?
            if play_button_rect.collidepoint(event.pos):
                game.start()