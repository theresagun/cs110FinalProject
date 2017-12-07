import pygame
import random

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, direction, color, gate):
         '''
        Initializes a ghost object with attributes: image, rect, rect.x, rect.y, speed, direction, wall_right, wall_below, wall_above, wall_left, collide_wall_list.
        '''
        #initializes the sprite class
        pygame.sprite.Sprite.__init__(self)
        #loads the image for the ghost
        self.image = pygame.image.load("assets/" + img_file).convert_alpha()
        #makes the ghost 15x15
        self.image = pygame.transform.scale(self.image, (15,15)).convert_alpha()
        #the rectangle for the ghost image
        self.rect = self.image.get_rect()
        #x value of rectangle
        self.rect.x = x
        #y value of rectangle
        self.rect.y = y
        #speed of the ghosts
        self.speed = 2
        #the initial direction of the ghost
        self.direction = direction
        #The variable that is changed if there is a wall right, below, above, or left of the ghost
        self.wall_right = False
        self.wall_below = False
        self.wall_above = False
        self.wall_left = False
        #the list that is appended to depending on how many walls are near the ghost
        self.collide_wall_list = []
        #the color state of the ghost
        self.color=color
        #1 or 2 depending of it the ghosts are in the gate or not respectively
        self.gate=gate

    def wallCollide(self, walls):
        '''
        Determines if the ghost collides with a wall.
        '''
        #loops through the list of wall sprites
        for wall in walls:
            #If the one of the ghosts sides is in a small radius of the walls side.
            #For example, if the ghost's right side is in a two pixel radius of the walls left side, then there is a wall to the right
            #of the ghost 
            if self.rect.midright[0] in range(wall.rect.midleft[0]-2, wall.rect.midleft[0]+2) and self.rect.midright[1] in range(wall.rect.midleft[1]-2, wall.rect.midleft[1]+2):
                self.wall_right = True
                self.collide_wall_list.append(self.wall_right)
                
            if self.rect.midtop[1] in range(wall.rect.midbottom[1]-2, wall.rect.midbottom[1]+2) and self.rect.midtop[0] in range(wall.rect.midbottom[0]-2, wall.rect.midbottom[0]+2):
                self.wall_above = True
                self.collide_wall_list.append(self.wall_above)
                
            if self.rect.midleft[0] in range(wall.rect.midright[0]-2, wall.rect.midright[0]+2) and self.rect.midleft[1] in range(wall.rect.midright[1]-2,wall.rect.midright[1]+2):
                self.wall_left = True
                self.collide_wall_list.append(self.wall_left)
                
            if self.rect.midbottom[1] in range(wall.rect.midtop[1]-2, wall.rect.midtop[1]+2) and self.rect.midbottom[0] in range(wall.rect.midtop[0]-2,wall.rect.midtop[0]+2):
                self.wall_below = True
                self.collide_wall_list.append(self.wall_below)

    def nodeCollide(self, nodes):
        '''
        Determines if ghost collides with a node.
        '''
        #If the ghost's center is equal to the nodes center, then the ghost is at a node
        for node in nodes:
           if self.rect.center == node.rect.center:
                 return True
        return False
 

    def move(self):
        '''
        Ghost moves based on set direction and speed.
        '''
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y -= self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y += self.speed

        
    def outsideMap(self):
        '''
        If ghost leaves the map, it will return from the opposide side.
        '''
        #420 is the right edge of the map and it changes his position to the other side
        if self.rect.midleft[0] > 420:
            self.rect.x = 1

        #14 is the left edge of the map and it changes his position to the other side
        elif self.rect.midright[0] < 15:
            self.rect.x = 405

    def oppositeDirection(self):
        '''
        Ghost reverses direction.
        '''
        if self.direction==0:
            self.direction=2
        elif self.direction==1:
            self.direction=3
        elif self.direction==2:
            self.direction=0
        elif self.direction==3:
            self.direction=1

    def inGateMove(self, walls):
        '''
        Ghost bounces in the box.
        '''
        #changes the wall variables if there is a wall above or below
        self.wallCollide(walls)

        #if there is a wall above, change the direction to down
        if self.wall_above:
            self.oppositeDirection()
            #moves the ghost up 2 so that it is no longer in the wall above range
            self.rect.y += 2

        #if there is a wall belowm change the direction to up
        elif self.wall_below:
            self.oppositeDirection()
            #moves the ghost down 2 so that is no longer in the wall below range
            self.rect.y -= 2

        #resets the wall values to be false
        self.wall_left = False
        self.wall_right = False
        self.wall_above = False
        self.wall_below = False
        self.collide_wall_list = []


   

    def update(self, nodes, walls):
        '''
        Determines which way the ghost goes.
        '''
        #If the ghost collides with a node
        if self.nodeCollide(nodes) == True:
            #changes the wall variables if there is a wall above or below
            self.wallCollide(walls)

            #if the length of the list is 0, that means that there are no walls around the ghost so it
            #can go any direction but backwards
            if len(self.collide_wall_list) == 0:
                if self.direction == 0:
                    self.direction = random.choice([0,1,3])
                elif self.direction == 1:
                    self.direction = random.choice([0,1,2])
                elif self.direction == 2:
                    self.direction = random.choice([1,2,3])
                elif self.direction == 3:
                    self.direction = random.choice([0,2,3])
            
            #If the length of the list is 1, that means that there is one wall in some direction of the ghost.
            #The ghost can then move any direction but in the direction of the wall or backwards.
            elif len(self.collide_wall_list) == 1:
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

            #If the length of the list is 2, then there are 2 walls around the ghost and the ghost is in a corner.
            #If the ghost is in a corner, it can only move one other direction that is not either of the 2 walls, or backwards
            elif len(self.collide_wall_list) == 2:
                #Makes a variable to determine where where the walls are.
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
        
        #Sets all of the wall variables to False to make sure that there is a new test every time.
        self.wall_below = False
        self.wall_right = False
        self.wall_left = False
        self.wall_above = False
        self.collide_wall_list = []

        

