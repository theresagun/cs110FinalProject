import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, state):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = state
    def update(self):
        pass
        

class Red(Ghost):
    def __init__(self):
        pass

class Blue(Ghost):
    def __init__(self):
        pass

class Orange(Ghost):
    def __init__(self):
        pass

class Pink(Ghost):
    def __init__(self):
        pass