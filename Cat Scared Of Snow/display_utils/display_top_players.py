import pygame
import sys

WIDTH, HEIGHT = 1000, 800
FPS = 60
WHITE = (255, 255, 255)


def display_top_players(screen, clock, top_players, score):
    font = pygame.font.Font(None, 36)
    top_scores_lines = []
    if score >= 300000:
        top_scores_lines.append("Congratulations! You won!")
    else:
        top_scores_lines.append(f"Sorry! You lost with score {score}. Better luck next time.")
        top_scores_lines.append("To win get at least 300000 points")
    top_scores_lines.append("")
    top_scores_lines.append("Top 5 Players:")

    for i, (player_name, player_score) in enumerate(top_players):
        formatted_name = f"{player_name: <10}"
        line = f"{i + 1}. {formatted_name}: {player_score} points"
        top_scores_lines.append(line)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)

        y_offset = HEIGHT // 2 - len(top_scores_lines) * 20 // 2

        for line in top_scores_lines:
            top_scores_surface = font.render(line, True, (0, 0, 0))
            screen.blit(top_scores_surface, (WIDTH // 2 - top_scores_surface.get_width() // 2, y_offset))
            y_offset += 30

        pygame.display.flip()
        clock.tick(FPS)
