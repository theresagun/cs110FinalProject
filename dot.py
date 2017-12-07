import pygame

class Dot(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, state):
        '''
        Initializes a dot object with attributes: image, rect, rect.x, rect.y, state.
        '''
        #initializes the sprite class
        pygame.sprite.Sprite.__init__(self)
        #loads the image for the dot
        self.image = pygame.image.load("assets/" + img_file).convert()
        #gets the rectangle of the surface
        self.rect = self.image.get_rect()
        #sets the x value of the rectangle
        self.rect.x = x
        #sets the y value of the rectangle
        self.rect.y = y
        #sets the state of the rectangle
        self.state = state
     
