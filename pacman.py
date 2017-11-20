import pygame

###pacman is always moving forward, we just need to determine which direction he is facing
###and whether or not he is hitting a wall.
class Pacman:
    def __init__(self, speed, position, screen):
        #"Surface(<width>, <height>)""
        #self.surface = pygame.Surface((200, 200))
        self.direction = "WEST"
        self.x = position[0]
        self.y = position[1]
        self.screen = screen
        self.surface = pygame.image.load("images/red-square.png").convert()
        self.speed = speed
    
    def getSurface(self):
        #blit draws a surface onto another surface.
        self.screen.blit(self.surface, (self.x, self.y))
    
    def moveSurface(self):
        #moves the surface by whatever the speed is set to.
        if self.direction == "WEST":
            self.x -= self.speed
        elif self.direction == "EAST":
            self.x += self.speed
        elif self.direction == "SOUTH":
            self.y -= self.speed
        elif self.direction == "NORTH":
            self.y += self.speed
    
    def turnSurface(self, direction):
        self.direction = direction
        
        
