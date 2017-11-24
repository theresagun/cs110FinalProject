import pygame

class Pacman(pygame.sprite.Sprite):
    pygame.sprite.Sprite.__init__(self)
    def __init__(self, x, y, img_file, direction):
        self.image = pygame.image.load("assets/" + img_file).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.lives = 3
        self.direction = direction
    
    def canMove(self, walls):
        #walls (list) - A group of all the wall sprites
        #loops through all the sprites in the walls list and if pacman collides with any of them
        #the function returns False because it means pacman cannot move
        for wall in walls:
            if wall.collide_rect(self.rect):
                return False
        return True
    
    def move(self):
        #moves the surface by whatever the speed is set to.
        #also when the direction is changed, the image direction should change too
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y += self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y -= self.speed
    
    #All the comments in this will probably not be actual code because I believe we can just
    #transform the image to be the direction we want it to be.
    def turnRight(self):
        self.direction = 0
        #self.image = pygame.image.load("assets/" + img_file + '_right').convert()
    def turnUp(self):
        self.direction = 1
        #self.image = pygame.image.load("assets/" + img_file + '_up').convert()
    def turnLeft(self):
        self.direction = 2
        #self.image = pygame.image.load("assets/" + img_file + '_left').convert()
    def turnDown(self):
        self.direction = 3
        #self.image = pygame.image.load("assets/" + img_file + '_down').convert()       
