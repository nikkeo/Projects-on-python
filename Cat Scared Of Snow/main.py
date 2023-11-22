import pygame
from businessLogic.game import game
from database.databaseManager import databaseManager

pygame.init()
dbmanager = databaseManager()

dbmanager.create_table()

game()

dbmanager.close_connection()