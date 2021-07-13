import pygame

normal_font = pygame.font.SysFont("", 32)
selected_font = pygame.font.SysFont("", 60)

color_black = (0, 0, 0)
color_red = (255, 0, 0)

def render_text(selection, target_selection, text):
    if selection == target_selection:
        text = selected_font.render(text, True, color_red)
    else:
        text = normal_font.render(text, True, color_black)
    return text
    