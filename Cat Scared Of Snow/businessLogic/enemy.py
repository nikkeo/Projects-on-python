import pygame
import random
import os
from businessLogic.consts import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = "enemy.webp"
        if os.path.isfile(image_path):
            original_image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(original_image, SIZE)
        else:
            self.image = pygame.Surface(SIZE)
            self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(ZERO, WIDTH - self.rect.width)
        self.rect.y = random.randint(ZERO, HEIGHT - self.rect.height)

    def update(self):
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(ZERO, WIDTH - self.rect.width)
            self.rect.y = ZERO