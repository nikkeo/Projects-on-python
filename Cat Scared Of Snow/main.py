import pygame
from businessLogic.game import game
from database.database_config import database_config

pygame.init()

database_config()

game()
