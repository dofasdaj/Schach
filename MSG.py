import pygame
def to_screen(msg,farbe,xpos,ypos,size,display):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, farbe)
    display.blit(screen_text,[xpos,ypos])
