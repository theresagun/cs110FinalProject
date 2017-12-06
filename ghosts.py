import pygame
import random

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, direction, color, gate):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (15,15)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.direction = direction
        self.wall_right = False
        self.wall_below = False
        self.wall_above = False
        self.wall_left = False
        self.collide_wall_list = []
        self.color=color
        self.gate=gate

 
 
     #def createTestSprites(self):
         #self.north = ghostTestSprite(self.rect.x, self.rect.y - 15)
         #self.south = ghostTestSprite(self.rect.x, self.rect.y + 15)
         #self.east = ghostTestSprite(self.rect.x + 15, self.rect.y)
         #self.west = ghostTestSprite(self.rect.x - 15, self.rect.y)

         #self.test_tiles = pygame.sprite.Group([self.north, self.south, self.east, self.west])

    def wallCollide(self, walls):
        '''
        for wall in walls:
           for tile in self.test_tiles:
                if pygame.sprite.collide_rect(wall, tile):
                    print(tile)
                    self.collide_tile_list.append(tile)
        '''
        for wall in walls:
            if self.rect.midright[0] in range(wall.rect.midleft[0]-2, wall.rect.midleft[0]+2) and self.rect.midright[1] in range(wall.rect.midleft[1]-2, wall.rect.midleft[1]+2):#self.rect.midright[0] + 1 == wall.rect.midleft[0] and self.rect.midright[1] == wall.rect.midleft[1]:
                
                self.wall_right = True
                self.collide_wall_list.append(self.wall_right)
                
                
            if self.rect.midtop[1] in range(wall.rect.midbottom[1]-2, wall.rect.midbottom[1]+2) and self.rect.midtop[0] in range(wall.rect.midbottom[0]-2, wall.rect.midbottom[0]+2):#self.rect.midtop[1] - 1 == wall.rect.midbottom[1] and self.rect.midtop[0] == wall.rect.midbottom[0]:
               
                self.wall_above = True
                self.collide_wall_list.append(self.wall_above)
            
                
            if self.rect.midleft[0] in range(wall.rect.midright[0]-2, wall.rect.midright[0]+2) and self.rect.midleft[1] in range(wall.rect.midright[1]-2,wall.rect.midright[1]+2):#self.rect.midleft[0] - 1  == wall.rect.midright[0] and self.rect.midleft[1] == wall.rect.midright[1]: 
                
                self.wall_left = True
                self.collide_wall_list.append(self.wall_left)
                
                
            if self.rect.midbottom[1] in range(wall.rect.midtop[1]-2, wall.rect.midtop[1]+2) and self.rect.midbottom[0] in range(wall.rect.midtop[0]-2,wall.rect.midtop[0]+2):#self.rect.midbottom[1] + 1 == wall.rect.midtop[1] and self.rect.midbottom[0] == wall.rect.midtop[0]:
                
                self.wall_below = True
                self.collide_wall_list.append(self.wall_below)


        #print (self.collide_wall_list)
        

        #if len(self.collide_tile_list) == 0:
            #return (False, self.collide_tile_list)
        #else:
            #return (True, self.collide_tile_list)

    def nodeCollide(self, nodes):
        for node in nodes:
           if self.rect.center == node.rect.center:
                 return True
        return False
 

    def move(self):

        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y -= self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y += self.speed

        
    def outsideMap(self):
        if self.rect.midleft[0] > 420:
            self.rect.x = 1
        elif self.rect.midright[0] < 15:
            self.rect.x = 405
        
    def turnRight(self):
        self.direction = 0
    def turnUp(self):
        self.direction = 1
    def turnLeft(self):
        self.direction = 2
    def turnDown(self):
        self.direction = 3

    def oppositeDirection(self):
        if self.direction==0:
            self.direction=2
        elif self.direction==1:
            self.direction=3
        elif self.direction==2:
            self.direction=0
        elif self.direction==3:
            self.direction=1


   

    def update(self, nodes, walls):
        if self.nodeCollide(nodes) == True:
            self.wallCollide(walls)
            
            if len(self.collide_wall_list) == 0:
                if self.direction == 0:
                    self.direction = random.choice([0,1,3])
                elif self.direction == 1:
                    self.direction = random.choice([0,1,2])
                elif self.direction == 2:
                    self.direction = random.choice([1,2,3])
                elif self.direction == 3:
                    self.direction = random.choice([0,2,3])
            elif len(self.collide_wall_list) == 1:
                #self.collide_tile1 = self.collide_tile_list[0]
                if self.wall_right == True:
                    if self.direction == 0:
                        self.direction = random.choice([1,3])
                    elif self.direction == 1:
                        self.direction = random.choice([1,2])
                    elif self.direction == 2:
                        self.direction = random.choice([1,2,3])
                    elif self.direction == 3:
                        self.direction = random.choice([2,3])
                elif self.wall_above == True:
                    if self.direction == 0:
                        self.direction = random.choice([0,3])
                    elif self.direction == 1:
                        self.direction = random.choice([0,2])
                    elif self.direction == 2:
                        self.direction = random.choice([2,3])
                    elif self.direction == 3:
                        self.direction = random.choice([0,2,3])
                elif self.wall_left == True:
                    if self.direction == 0:
                        self.direction = random.choice([0,1,3])
                    elif self.direction == 1:
                        self.direction = random.choice([0,1])
                    elif self.direction == 2:
                        self.direction = random.choice([1,3])
                    elif self.direction == 3:
                        self.direction = random.choice([0,3])
                elif self.wall_below == True:
                    if self.direction == 0:
                        self.direction = random.choice([0,1])
                    elif self.direction == 1:
                        self.direction = random.choice([0,1,2])
                    elif self.direction == 2:
                        self.direction = random.choice([1,2])
                    elif self.direction == 3:
                        self.direction = random.choice([0,2])
                #determine state of the tile then make a random choice that is not the
                #direction the tile is in or backwards
            elif len(self.collide_wall_list) == 2:
                #self.collide_tile1 = self.collide_tile_list[0]
                #self.collide_tile2 = self.collide_tile_list[1]
                self.bot_right = self.wall_below and self.wall_right
                self.top_right = self.wall_above and self.wall_right
                self.top_left = self.wall_above and self.wall_left
                self.bot_left = self.wall_below and self.wall_left
                if self.bot_right:
                    if self.direction == 3:
                        self.direction = 2
                    elif self.direction == 0:
                        self.direction = 1
                elif self.top_right:
                    if self.direction == 1:
                        self.direction = 2
                    elif self.direction == 0:
                        self.direction = 3
                elif self.top_left:
                    if self.direction == 1:
                        self.direction = 0
                    elif self.direction == 2:
                        self.direction = 3
                elif self.bot_left:
                    if self.direction == 3:
                        self.direction = 0
                    elif self.direction == 2:
                        self.direction = 1
                #determine the state of each tile then go the only direction that
                #is available
        self.wall_below = False
        self.wall_right = False
        self.wall_left = False
        self.wall_above = False
        self.collide_wall_list = []

        

