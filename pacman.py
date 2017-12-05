import pygame
import wall1

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert()
        self.image = pygame.transform.scale(self.image, (15,15))
        self.choose_list=1
        self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        #if self.choose_list==1:
         #   self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        #if self.choose_list==2:
         #   self.rotated_list=["assets/steven-right.jpg","assets/steven-up.jpg","assets/steven-left.jpg", "assets/steven-down.jpg"]
        #if self.image=="pacman1.png":
         #   self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        #else: 
         #   self.rotated_list=["assets/steven-right.jpg","assets/steven-up.jpg","assets/steven-left.jpg", "assets/steven-down.jpg"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.lives = 3
        self.direction = direction

    def choose_img(self):
    '''
    Decides which image to display for Pacman character based on the selected mode.
    '''
        if self.choose_list==1:
            self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        else:
            self.rotated_list=["assets/steven-right.jpg","assets/steven-up.png","assets/steven-right.png", "assets/steven-down.png"]

    
    def canMove(self, walls):
    '''
    Determines if Pacman character can move based on its location relative to the walls.
    '''
        #walls (list) - A group of all the wall sprites
        #loops through all the sprites in the walls list and if pacman collides with any of them
        #the function returns False because it means pacman cannot move
        #for wall in walls:
           # if pygame.sprite.collide_mask(self.mask, pygame.mask.from_surface(wall.image)):
               # return False
        #return True
        #for wall in walls:
            #if wall.collide_rect(self.rect):
        if pygame.sprite.spritecollide(self, walls, False):
                return False
        return True
    
    def nodeCollide(self, nodes):
    '''
    Determines if Pacman character has reached an intersection.
    '''
        for node in nodes:
            if self.rect.centerx in range(node.rect.centerx - 5, node.rect.centerx + 5) and self.rect.centery in range(node.rect.centery - 5, node.rect.centery + 5):
                return (True, node)
        
        return (False, None)

    def dotCollide(self, dots):
    '''
    Determines if Pacman character has collided with a dot.
    '''
        for dot in dots:
            if self.rect.centerx in range(dot.rect.centerx - 5, dot.rect.centerx + 5) and self.rect.centery in range(dot.rect.centery - 5, dot.rect.centery + 5):
                return (True, dot)
        return (False, None)
    
    def bigDotCollide(self, dots):
    '''
    Determines if Pacman character has collided with a big dot.
    '''
        for dot in dots:
           if self.rect.centerx in range(dot.rect.centerx - 5, dot.rect.centerx + 5) and self.rect.centery in range(dot.rect.centery - 5, dot.rect.centery + 5):
                return (True, dot)
        return (False, None)



    def correctTurn(self, dot):
        self.rect.centerx = dot.rect.centerx
        self.rect.centery = dot.rect.centery

    def move(self):
    '''
    Moves the surface based on set direction and speed.
    '''
        #moves the surface by whatever the speed is set to.
        #also when the direction is changed, the image direction should change too
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y -= self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y += self.speed
        
    
    #All the comments in this will probably not be actual code because I believe we can just
    #transform the image to be the direction we want it to be.


    def turnRight(self):
    '''
    Pacman character turns right.
    '''
        self.direction = 0
        self.rotated_img=pygame.image.load(self.rotated_list[0]).convert()
       
        #self.image = pygame.image.load("assets/" + img_file + '_right').convert()
    def turnUp(self):
    '''
    Pacman character turns up.
    '''
        self.direction = 1
        self.rotated_img=pygame.image.load(self.rotated_list[1]).convert()
        
        #self.image = pygame.image.load("assets/" + img_file + '_up').convert()
    def turnLeft(self):
    '''
    Pacman character turns left.
    '''
        self.direction = 2
        self.rotated_img=pygame.image.load(self.rotated_list[2]).convert()
        
        #self.image = pygame.image.load("assets/" + img_file + '_left').convert()
    def turnDown(self):
    '''
    Pacman character turns down.
    '''
        self.direction = 3
        self.rotated_img=pygame.image.load(self.rotated_list[3]).convert()     
        
        #self.image = pygame.image.load("assets/" + img_file + '_down').convert()       
