import os
import pygame
from businessLogic.consts import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        image_path = "hero.jpeg"
        if os.path.isfile(image_path):
            original_image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(original_image, SIZE)
        else:
            self.image = pygame.Surface(SIZE)
            self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self, *args, **kwargs):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > ZERO:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += PLAYER_SPEED
        if keys[pygame.K_UP] and self.rect.top > ZERO:
            self.rect.y -= PLAYER_SPEED
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += PLAYER_SPEED