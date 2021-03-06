import pygame
import wall1

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, direction):
        '''
        Initializes a Pacman object with attributes: image, rect, rect.x, rect.y, speed, lives, direction.
        '''
        #intialize the sprite
        pygame.sprite.Sprite.__init__(self)
        #loads the image and creates a surface
        self.image = pygame.image.load("assets/" + img_file).convert_alpha()
        #scales the image to be the same as the tile size which is 15x15
        self.image = pygame.transform.scale(self.image, (15,15)).convert_alpha()
        #default image state
        self.choose_list=1
        #list of all the names of all the images for each direction of pacman
        self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        #the rectangle of the surface
        self.rect = self.image.get_rect()
        #x value of rectangle
        self.rect.x = x
        #y value of rectangle
        self.rect.y = y
        #default speed of pacman
        self.speed = 2
        #amount of lives pacman has
        self.lives = 3
        #direction that pacman is facing when created
        self.direction = direction

    def chooseImg(self):
        '''
        Determines which Pacman image to use depending on which mode was chosen.
        '''
        if self.choose_list==1:
            #list of regular pacman images
            self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        else:
            #list of steven as the pacman images
            self.rotated_list=["assets/steven-right.jpg","assets/steven-up.png","assets/steven-right.png", "assets/steven-down.png"]

    
    def canMove(self, walls):
        '''
        Determines if Pacman can move based on his location relative to the walls.
        '''
        if pygame.sprite.spritecollide(self, walls, False):
                return False
        return True
    
    def nodeCollide(self, nodes):
        '''
        Determines if Pacman collides with a node.
        '''
        for node in nodes:
            #if pacman is in a certain radius around the center of the node, then he is colliding with the node
            if self.rect.centerx in range(node.rect.centerx - 5, node.rect.centerx + 5) and self.rect.centery in range(node.rect.centery - 5, node.rect.centery + 5):
                return (True, node)
        return (False, None)

    def dotCollide(self, dots):
        '''
        Determines if Pacman collides with a dot.
        '''
        for dot in dots:
            #if pacman is in a certain radius around the center of the dot, then he is colliding with the dot
            if self.rect.centerx in range(dot.rect.centerx - 5, dot.rect.centerx + 5) and self.rect.centery in range(dot.rect.centery - 5, dot.rect.centery + 5):
                return (True, dot)
        return (False, None)
    
    def bigDotCollide(self, dots):
        '''
        Determines if Pacman collides with a big dot.
        '''
        for dot in dots:
             #if pacman is in a certain radius around the center of the dot, then he is colliding with the dot
           if self.rect.centerx in range(dot.rect.centerx - 5, dot.rect.centerx + 5) and self.rect.centery in range(dot.rect.centery - 5, dot.rect.centery + 5):
                return (True, dot)
        return (False, None)

    def ghostCollide(self, ghosts):
        '''
        Determines if Pacman collides with a ghost.
        '''
        for ghost in ghosts:
             #if pacman is in a certain radius around the center of the ghost, then he is colliding with the ghost
           if self.rect.centerx in range(ghost.rect.centerx - 5, ghost.rect.centerx + 5) and self.rect.centery in range(ghost.rect.centery - 5, ghost.rect.centery + 5):
                return (True, ghost)
        return (False, None)
 
    def outsideMap(self):
        '''
        If Pacman goes off the map on one side, he will return on the other.
        '''
        #420 is the right edge of the map and it changes his position to the other side
        if self.rect.midleft[0] > 420:
            self.rect.x = 1
        #14 is the left edge of the map and it changes his position to the other side
        elif self.rect.midright[0] < 15:
            self.rect.x = 405
        

    def correctTurn(self, dot):
        '''
        Puts Pacman in the center of the path after turning.
        '''
        self.rect.centerx = dot.rect.centerx
        self.rect.centery = dot.rect.centery

    def move(self):
        '''
        Pacman character moves according to set speed and direction.
        '''
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y -= self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y += self.speed

    def turnRight(self):
        '''
        Pacman character turns to the right, image turns to the right.
        '''
        self.direction = 0
        self.rotated_img=pygame.image.load(self.rotated_list[0]).convert_alpha()
       
    def turnUp(self):
        '''
        Pacman character turns up, image turns up.
        '''
        self.direction = 1
        self.rotated_img=pygame.image.load(self.rotated_list[1]).convert_alpha()
        
    def turnLeft(self):
        '''
        Pacman character turns to the left, image turns to the left.
        '''
        self.direction = 2
        self.rotated_img=pygame.image.load(self.rotated_list[2]).convert_alpha()
        
    def turnDown(self):
        '''
        Pacman character turns down, image turns down.
        '''
        self.direction = 3
        self.rotated_img=pygame.image.load(self.rotated_list[3]).convert_alpha()     
              
