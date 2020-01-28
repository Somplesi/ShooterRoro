import pygame
from player import Player


# Créer la Classe du jeu
class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}
