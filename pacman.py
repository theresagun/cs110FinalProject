import pygame
import wall1

class Pacman(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, direction):
        '''
        Initializes a Pacman object with attributes: image, rect, rect.x, rect.y, speed, lives, direction.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (15,15)).convert_alpha()
        self.choose_list=1
        self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

        self.lives = 3
        self.direction = direction

    def chooseImg(self):
        '''
        Determines which Pacman image to use depending on which mode was chosen.
        '''
        if self.choose_list==1:
            self.rotated_list=["assets/pacman-right.png","assets/pacman-up.png","assets/pacman-left.png", "assets/pacman-down.png"]
        else:
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
            if self.rect.centerx in range(node.rect.centerx - 5, node.rect.centerx + 5) and self.rect.centery in range(node.rect.centery - 5, node.rect.centery + 5):
                return (True, node)
        
        return (False, None)

    def dotCollide(self, dots):
        '''
        Determines if Pacman collides with a dot.
        '''
        for dot in dots:
            if self.rect.centerx in range(dot.rect.centerx - 5, dot.rect.centerx + 5) and self.rect.centery in range(dot.rect.centery - 5, dot.rect.centery + 5):
                return (True, dot)
        return (False, None)
    
    def bigDotCollide(self, dots):
        '''
        Determines if Pacman collides with a big dot.
        '''
        for dot in dots:
           if self.rect.centerx in range(dot.rect.centerx - 5, dot.rect.centerx + 5) and self.rect.centery in range(dot.rect.centery - 5, dot.rect.centery + 5):
                return (True, dot)
        return (False, None)

    def ghostCollide(self, ghosts):
        '''
        Determines if Pacman collides with a ghost.
        '''
        for ghost in ghosts:
           if self.rect.centerx in range(ghost.rect.centerx - 5, ghost.rect.centerx + 5) and self.rect.centery in range(ghost.rect.centery - 5, ghost.rect.centery + 5):
                return (True, ghost)
        return (False, None)
 
    def outsideMap(self):
        '''
        If Pacman goes off the map on one side, he will return on the other.
        '''
        if self.rect.midleft[0] > 420:
            self.rect.x = 1
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
