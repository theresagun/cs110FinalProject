import pygame

class Pacman:
    def __init__(self):
        #"Surface(<width>, <height>)""
        #self.surface = pygame.Surface((200, 200))
        self.x = 0
        self.y = 0
        self.surface = pygame.image.load("images/red-square.png").convert()
    
    def getSurface(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    
    def moveSurface(self, screen):
        self.x += 1
        