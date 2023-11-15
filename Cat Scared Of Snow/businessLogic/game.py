import pygame
import sys
from businessLogic.player import Player
from businessLogic.enemy import Enemy
from display_utils.display_top_players import display_top_players
from display_utils.input_name_screen import input_name_screen
from database.get_top_players import get_top_players
from database.add_score import add_score

WIDTH, HEIGHT = 1000, 800
FPS = 60
WHITE = (255, 255, 255)


def game():
    pygame.display.set_caption("Cat Scared Of Snow")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)

    player_name, screen, clock = input_name_screen(screen, clock)

    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    player = Player()
    all_sprites.add(player)

    for _ in range(5):
        enemy = Enemy()
        while pygame.sprite.spritecollideany(enemy, all_sprites):
            enemy = Enemy()
        all_sprites.add(enemy)
        enemies.add(enemy)

    running = True
    score = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.update(keys)

        all_sprites.update()

        hits = pygame.sprite.spritecollide(player, enemies, False)
        if hits:
            add_score(player_name, score)
            top_players = get_top_players()
            display_top_players(screen, clock, top_players, score)
            running = False

        screen.fill(WHITE)
        all_sprites.draw(screen)

        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

        clock.tick(FPS)
        score += 1

    pygame.quit()
    sys.exit()
