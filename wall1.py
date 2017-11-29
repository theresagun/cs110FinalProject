import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #print(self.rect.x)
