import pygame

from dino_runner.utils.constants import ICON, SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = 'freesansbold.ttf'
BLACK_COLOR = (0, 0, 0)

def get_score_elements(points):
    font  = pygame.font.Font(FONT_STYLE, 20)
    text = font.render(f"Points: {points}", True, BLACK_COLOR )
    text_rect = text.get_rect()
    text_rect.center = (1000, 35)
    return text, text_rect

def get_centered_message(message):
    font  = pygame.font.Font(FONT_STYLE, 50)
    text = font.render(message, True, BLACK_COLOR )
    text_rect = text.get_rect()
    text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2.3)
    return text, text_rect

def get_score_deaths(deaths):
    font  = pygame.font.Font(FONT_STYLE, 40)
    text = font.render(f"Deaths: {deaths}", True, BLACK_COLOR )
    text_rect = text.get_rect()
    text_rect.center = (520, 400)
    return text, text_rect

def get_last_score(points_menu):
    font  = pygame.font.Font(FONT_STYLE, 40)
    text = font.render(f"Last points: {points_menu}", True, BLACK_COLOR )
    text_rect = text.get_rect()
    text_rect.center = (520, 450)
    return text, text_rect

def get_best_score(best_points):
    font  = pygame.font.Font(FONT_STYLE, 40)
    text = font.render(f"Best points: {best_points}", True, BLACK_COLOR )
    text_rect = text.get_rect()
    text_rect.center = (520, 500)
    return text, text_rect

def dinosaur_icon():
    text = ICON
    text_rect = text.get_rect()
    text_rect.center = (520, 150)
    return text, text_rect
