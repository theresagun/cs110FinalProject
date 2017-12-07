import pygame

class Node(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file):
        '''
        Initializes a node object with attributes: image, rect, rec.x, rect.y.
        '''
        #initializes the sprite class
        pygame.sprite.Sprite.__init__(self)
        #loads the image for the node (only used for testing)
        self.image = pygame.image.load("assets/" + img_file).convert()
        #sets the image to be the tile size 15x15
        self.image = pygame.transform.scale(self.image, (15, 15))
        #gets the rectangle for image surface
        self.rect = self.image.get_rect()
        #sets the x value for the rectangle
        self.rect.x = x
        #sets the y value for the rectangle
        self.rect.y = y