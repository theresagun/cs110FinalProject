import pygame

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/" + img_file).convert()
        self.image = pygame.transform.scale(self.image, (15,15))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 1
        self.direction = direction
        self.north = ghostTestSprite(self.rect.x, self.rect.y - 15, 1)
        self.south = ghostTestSprite(self.rect.x, self.rect.y + 15, 3)
        self.east = ghostTestSprite(self.rect.x + 15, self.rect.y, 2)
        self.west = ghostTestSprite(self.rect.x - 15, self.rect.y, 0)
        self.test_tiles = pygame.sprite.Group([self.north, self.south, self.east, self.west])
        self.test_tiles_list = self.test_tiles.sprites()
        print(self.test_tiles_list)
 
 
     #def createTestSprites(self):
         #self.north = ghostTestSprite(self.rect.x, self.rect.y - 15)
         #self.south = ghostTestSprite(self.rect.x, self.rect.y + 15)
         #self.east = ghostTestSprite(self.rect.x + 15, self.rect.y)
         #self.west = ghostTestSprite(self.rect.x - 15, self.rect.y)

         #self.test_tiles = pygame.sprite.Group([self.north, self.south, self.east, self.west])

    def wallCollide(self, walls):
        for wall in walls:
            for tile in self.test_tiles:
                if pygame.sprite.collide_rect(wall,tile):
                    return (True, tile)
        return (False, None)
			
 

    def nodeCollide(self, nodes):
        for node in nodes:
           if self.rect.center == node.rect.center:
                 return (True, node)
        return (False, None)
 

    def move(self):
        if self.direction == 0:
            self.rect.x += self.speed
        elif self.direction == 1:
            self.rect.y -= self.speed
        elif self.direction == 2:
            self.rect.x -= self.speed
        elif self.direction == 3:
            self.rect.y += self.speed
                
        self.north.update(self.rect.x, self.rect.y - 15)
        self.south.update(self.rect.x, self.rect.y + 15)
        self.east.update(self.rect.x + 15, self.rect.y)
        self.west.update(self.rect.x - 15, self.rect.y)

    def turnRight(self):
        self.direction = 0
    def turnUp(self):
        self.direction = 1
    def turnLeft(self):
        self.direction = 2
    def turnDown(self):
        self.direction = 3


    def update(self):
        pass
        
class ghostTestSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, state):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((15,15))
        self.image.fill((150,150,150))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = state
    
    def update(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Red(Ghost):
    def __init__(self):
        pass

class Blue(Ghost):
    def __init__(self):
        pass

class Orange(Ghost):
    def __init__(self):
        pass

class Pink(Ghost):
    def __init__(self):
        pass
