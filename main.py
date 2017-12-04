import pygame
import pacman
import maps
import ghosts
import random
import sys


class Controller:
    def __init__ (self, width=1050, height=1050):
        pygame.init()
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.caption=pygame.display.set_caption('Pacman')
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.Pacman=pacman.Pacman(315,315, "pacman1.png" , 3)
        self.Ghost = ghosts.Ghost(315, 315, 'blueghost.png', 1)
     
        #self.screen.blit(self.Pacman, (480,520))
        #self.Pacman.getSurface()
        self.create_map=maps.Map((300,300), 15)
        
        #self.sprites=pygame.sprite.Group((self.map_background)+ (self.Pacman))
        self.pacman_sprite=pygame.sprite.Group(self.Pacman)
        self.ghost_sprite=pygame.sprite.Group(self.Ghost)
        
        #adding walls to a sprite group & putting them on screen

        self.map_background=maps.Map.load_map(self.create_map)
        self.wall_sprites = pygame.sprite.Group(self.map_background[0])
        self.dot_sprites = pygame.sprite.Group(self.map_background[1])
        self.node_sprites = pygame.sprite.Group(self.map_background[2])
        #print(self.map_background)
    #    for walls in self.wall_sprites: 
     #         walls.draw(self.screen)
#             wall_image=walls[2]
              
            # self.screen.blit(walls)
			
  #          self.wall_sprites.add(walls)


    def startMenu(self):
        while True:
            self.background.fill((0, 0, 0))
            
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            img = pygame.image.load('assets/logo.png')
            img=pygame.transform.scale(img, (500,100))
            red_rect=pygame.image.load("assets/red-rect.png")
            red_rect=pygame.transform.scale(red_rect, (200,100))
            map_pic=pygame.image.load("assets/opening -pic.jpg")
            map_pic=pygame.transform.scale(map_pic, (250,250))


            left1 = pygame.font.SysFont("Times New Roman", 30)
            left_mode_top=left1.render('Press Left Key ', False, (0, 0, 0))
            left_mode_bottom=left1.render("For Mode 1", False, (0,0,0))


            
            right1 = pygame.font.SysFont("Times New Roman", 30)
            right_mode_top=right1.render('Press Right Key ', False, (0, 0, 0))
            right_mode_bottom=right1.render("For Mode 2", False, (0,0,0))
            
            


            self.screen.blit(self.background, (0, 0))
            self.screen.blit(img,(245,0))
            self.screen.blit(red_rect,(150,450))
            self.screen.blit(red_rect,(650,450))

            self.screen.blit(left_mode_top, (165,460))
            self.screen.blit(left_mode_bottom, (175,490))
            self.screen.blit(right_mode_top, (660,460))
            self.screen.blit(right_mode_bottom, (675,490))
            self.screen.blit(map_pic, (370,400))
              

            pygame.display.flip()    



    def gameLoop(self):
        pygame.key.set_repeat(1,60)
        while True:
            self.background.fill((0, 0, 0))
            self.dot_collide_tuple = self.Pacman.nodeCollide(self.node_sprites)
            self.dot_is_colliding = self.dot_collide_tuple[0]
            self.colliding_dot = self.dot_collide_tuple[1]
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnUp()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    elif event.key == pygame.K_DOWN and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnDown()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    elif event.key == pygame.K_RIGHT and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnRight()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (self.Pacman.rect.x, self.Pacman.rect.y))
                    elif event.key == pygame.K_LEFT and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnLeft()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    if event.key == pygame.K_UP and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 3:
                        self.Pacman.turnUp()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    elif event.key == pygame.K_DOWN and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 1:
                        self.Pacman.turnDown()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    elif event.key == pygame.K_RIGHT and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 2:
                        self.Pacman.turnRight()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    elif event.key == pygame.K_LEFT and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 0:
                        self.Pacman.turnLeft()
                        self.Pacman.speed = 1
                        #self.screen.blit(self.Pacman.rotated_img, (100,100))
                    '''
                    else: 
                        if event.key == pygame.K_UP:
                            self.Pacman.rect.y+100
                            self.Pacman.speed=0
                            #if event.type==pygame.KEYUP:  
                            #   self.Pacman.canMove(self.wall_sprites)==True
                        elif event.key == pygame.K_DOWN:
                            self.Pacman.rect.y-100
                            self.Pacman.speed=0
                            
                        elif event.key == pygame.K_RIGHT:     
                            self.Pacman.rect.x-100 
                            self.Pacman.speed=0                            
                        elif event.key == pygame.K_LEFT:
                            self.Pacman.rect.x+100
                            self.Pacman.speed=0  
                    '''  
            self.ghost_collide_tuple = self.Ghost.nodeCollide(self.node_sprites)
            self.ghost_collide = self.ghost_collide_tuple[0]
            self.ghost_tiles_collide = self.Ghost.wallCollide(self.wall_sprites)
            if self.ghost_collide:
                if self.Ghost.direction == 0:
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 0:
                        self.Ghost.direction = random.choice([1,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 2:
                        self.Ghost.direction = random.choice([0,1,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 1:
                        self.Ghost.direction = random.choice([0,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 3:
                        self.Ghost.direction = random.choice([0,1])
                elif self.Ghost.direction == 1:
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 0:
                        self.Ghost.direction = random.choice([1,2])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 2:
                        self.Ghost.direction = random.choice([0,1])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 1:
                        self.Ghost.direction = random.choice([0,2])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 3:
                        self.Ghost.direction = random.choice([0,1,2])
                elif self.Ghost.direction == 2:
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 0:
                        self.Ghost.direction = random.choice([1,2,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 2:
                        self.Ghost.direction = random.choice([1,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 1:
                        self.Ghost.direction = random.choice([2,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 3:
                        self.Ghost.direction = random.choice([1,2])
                elif self.Ghost.direction == 3:
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 0:
                        self.Ghost.direction = random.choice([2,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 2:
                        self.Ghost.direction = random.choice([0,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 1:
                        self.Ghost.direction = random.choice([0,2,3])
                    if self.ghost_tiles_collide[0] and self.ghost_tiles_collide[1].state == 3:
                        self.Ghost.direction = random.choice([0,2])

            self.Ghost.move()
                
                    
            if self.Pacman.canMove(self.wall_sprites):
                self.Pacman.move()
            else:
                if self.Pacman.direction == 0:
                    self.Pacman.rect.x -= 1
                    self.Pacman.speed = 0
                elif self.Pacman.direction == 1:
                    self.Pacman.rect.y += 1
                    self.Pacman.speed = 0
                elif self.Pacman.direction == 2:
                    self.Pacman.rect.x += 1
                    self.Pacman.speed = 0
                elif self.Pacman.direction == 3:
                    self.Pacman.rect.y -= 1
                    self.Pacman.speed = 0
                        
                    #else:
                        #direction=self.Pacman.direction
                        #direction=event.key
                        #speed=self.Pacman.speed
                        #self.Pacman.speed=0
                     #   if event.key != direction:
                           #self.Pacman.speed=speed
                      #     if event.key == pygame.K_UP:
                        #       self.Pacman.turnUp()
                       #    elif event.key == pygame.K_DOWN:
                         #      self.Pacman.turnDown()
                         #  elif event.key == pygame.K_RIGHT:
            	         #     self.Pacman.turnRight()                                                     
                          # elif event.key == pygame.K_LEFT:
                           #    self.Pacman.turnLeft()
                         
                 



                #elif self.Pacman.canMove(self.wall_sprites)==False:   
                 #    if event.type == pygame.KEYDOWN:
                  #     direction=self.Pacman.direction
                   #    speed=self.Pacman.speed
                    #   if event.key == pygame.K_UP:
                       #    self.Pacman.turnUp()
                      # elif event.key == pygame.K_DOWN:
                       #    self.Pacman.turnDown()
                      # elif event.key == pygame.K_RIGHT:
                       #    self.Pacman.turnRight()                                                     
                      # elif event.key == pygame.K_LEFT:
                     #      self.Pacman.turnLeft()
                   
                
                

                #if score.Score.lives==0
		    #GAME OVER

                   
            self.screen.blit(self.background, (0, 0))
            self.dot_sprites.draw(self.screen)
            self.node_sprites.draw(self.screen)
            self.wall_sprites.draw(self.screen)
            self.ghost_sprite.draw(self.screen)
            self.Ghost.test_tiles.draw(self.screen)
            self.pacman_sprite.draw(self.screen)
            pygame.display.flip()    

def main():
    main_window = Controller()
    main_window.gameLoop()
main()		
		
	







#Creates the color white as a tuple of 3 RGB values
#WHITE = (255, 255, 255)

#initialise pygame engine/libray
#pygame.init()

#The size(in pixels) of the window
#size = (700, 500)

#Creating the window in which the game is played
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption('Pacman')

#Boolean which keeps the game going or stops it
#carryOn = True

#used to control how fast screen updates
#clock = pygame.time.Clock()

#character = pacman.Pacman(1,(0,0), screen)

#while carryOn:
    #gets the users events
    #for event in pygame.event.get():
      #  if event.type == pygame.QUIT:
          #  carryOn = False
       # if event.type == pygame.K_DOWN:
          #  character.turnSurface('SOUTH')
	
    
    #Calls pacman's moveSurface() method which adds 1 to his x value
    #character.moveSurface()

    #fills the screen in white and clears the previous frame's canvas
    #screen.fill(WHITE)
    
    #Places pacman onto the screen using the blit pygame method
    #character.getSurface()

    #updates screen
    #pygame.display.flip()

    #limits to 60 fps
    #clock.tick(60)

#pygame.quit()
