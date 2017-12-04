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

    def nodeCollide(self, nodes):
        for node in nodes:
            if self.rect.centerx in range(node.rect.centerx - 5, node.rect.centerx + 5) and self.rect.centery in range(node.rect.centery - 5, node.rect.centery + 5):
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