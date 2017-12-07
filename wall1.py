import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        '''
        Initializes a wall object with attributes: image, rect, rect.x, rect.y.
        '''
        #initializes the sprite class
        pygame.sprite.Sprite.__init__(self)
        #loads the image for the walls
        self.image = pygame.image.load("assets/" + img_file).convert()
        #sets the image to the right size which is 15x15
        self.image = pygame.transform.scale(self.image, (15,15))
        #gets the rectangle for the image surface
        self.rect = self.image.get_rect()
        #sets the x value for the rectangle
        self.rect.x = x
        #sets the y value for the rectangle
        self.rect.y = y
