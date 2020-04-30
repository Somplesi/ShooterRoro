import pygame
from game import Game
pygame.init()


# Générer la fenêtre du jeu
pygame.display.set_caption("Comet fall Game HD")
screen = pygame.display.set_mode((1080, 720))

# Charger l'arrière-plan
background = pygame.image.load('assets/bg.jpg')

# Charger le jeu
game = Game()

running = True

while running:
    # Appliquer la fenêtre du jeu
    screen.blit(background, (0, -200))
    # Appliquer l'image du joueur
    screen.blit(game.player.image, game.player.rect)
    # Appliquer barre de vie du joueur
    game.player.update_health_bar(screen)
    
    # Recuperer projectile
    for projectile in game.player.all_projectiles:
        projectile.move()
    
    # Récupérer les Monstres
    for monster in game.all_monsters:
        monster.forward()
        monster.update_health_bar(screen)

    # Dessiner Image projectiles
    game.player.all_projectiles.draw(screen)
    
    # Dessiner Groupe de monstre
    game.all_monsters.draw(screen)
    
    # Vérifier si à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

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