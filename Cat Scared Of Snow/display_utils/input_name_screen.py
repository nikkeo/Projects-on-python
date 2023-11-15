import pygame
import sys

WIDTH, HEIGHT = 1000, 800
FPS = 60
WHITE = (255, 255, 255)


def input_name_screen(screen, clock):
    screen_rect = screen.get_rect()

    prompt_font = pygame.font.Font(None, 36)
    input_font = pygame.font.Font(None, 48)

    line1_text = prompt_font.render("Welcome to Cat Scared Of Snow", True, (0, 0, 0))
    line2_text = prompt_font.render("To win get 300000 points", True, (0, 0, 0))
    line3_text = prompt_font.render("Enter your nickname", True, (0, 0, 0))

    total_height = line1_text.get_height() + line2_text.get_height() + line3_text.get_height()

    center_y = HEIGHT // 2

    line1_rect = line1_text.get_rect(midtop=(screen_rect.centerx, center_y - total_height // 2))
    line2_rect = line2_text.get_rect(midtop=(screen_rect.centerx, line1_rect.bottom + 5))
    line3_rect = line3_text.get_rect(midtop=(screen_rect.centerx, line2_rect.bottom + 5))

    input_box = pygame.Rect(0, 0, 350, 40)
    input_box.center = (screen_rect.centerx, line3_rect.bottom + 50)

    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text.strip(), screen, clock
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill(WHITE)

        screen.blit(line1_text, line1_rect)
        screen.blit(line2_text, line2_rect)
        screen.blit(line3_text, line3_rect)

        txt_surface = input_font.render(text, True, color)
        width = max(350, txt_surface.get_width() + 10)
        input_box.w = width

        clipped_surface = pygame.Surface((input_box.w, input_box.h), pygame.SRCALPHA)
        clipped_surface.blit(txt_surface, (0, 0), (0, 0, input_box.w, input_box.h))
        screen.blit(clipped_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(FPS)