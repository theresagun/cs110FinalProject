import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        '''
        Initializes wall object with attributes: image, rect, rect.x, rect.y.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
