import pygame
import pacman
import maps
import ghosts
import random
import sys
import json



class Controller:
    def __init__ (self, width=1050, height=1050):
        pygame.init()
        pygame.mixer.init()
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.caption=pygame.display.set_caption('Pacman')
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.state="Start"
        self.mode=1
        
        self.ready=False
        #if self.mode==1:
         #   self.img="pacman1.png"
        #else:
         #   self.img="steven.jpg"
        self.Pacman=pacman.Pacman(200,479, "pacman1.png", 2)
        
        self.Ghost = ghosts.Ghost(315, 315, 'blueghost.png', 1)


        #self.high_score={'High Score': '0'}
        #high_score_json=json.dumps(self.high_score)
        
        
        self.current_score=0
        #self.high_score_file=open("assets/highScore.txt", "w")
        #self.score_words="{'High Score': '0'}" 
        #self.words_json=json.dumps(self.score_words)
        #self.high_score_file.write(self.words_json)
 
        #self.high_score_dict=json.loads(self.high_score_file.readline().strip())
        #self.high_score=self.high_score_json[1]
        #print(self.high_score)
        
        #self.high_score_file.close()
        self.high_score_file=open("assets/highScore.txt", "r")
        self.high_score=self.high_score_file.readline().strip()
        self.timer=True
     

        self.create_map=maps.Map((300,300), 15)
        
        #self.sprites=pygame.sprite.Group((self.map_background)+ (self.Pacman))
        self.pacman_sprite=pygame.sprite.Group(self.Pacman)
        self.ghost_sprite=pygame.sprite.Group(self.Ghost)
        
        #adding walls to a sprite group & putting them on screen

        self.map_background=maps.Map.load_map(self.create_map)
        self.wall_sprites = pygame.sprite.Group(self.map_background[0])
        self.dot_sprites = pygame.sprite.Group(self.map_background[1])
        self.node_sprites = pygame.sprite.Group(self.map_background[2])
        self.big_dot_sprites=pygame.sprite.Group(self.map_background[3])
        print(self.node_sprites)



    def startMenu(self):
        while True:
            self.background.fill((0, 0, 0))
            
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                
                     if event.key == pygame.K_LEFT:
                         self.state="Game"
                         self.mode=1
                         #self.Pacman=pacman.Pacman(200,479, "pacman1.png", 2)
                         #self.pacman_sprite=pygame.sprite.Group(self.Pacman)
                         #self.Pacman.image=pygame.image.load("assets/pacman1.png")
                         self.Pacman.choose_list=1
                         self.Pacman.choose_img()
                         self.startGameLoop()
                     if event.key == pygame.K_RIGHT:
                         self.state="Game"
                         self.mode=2
                         #self.Pacman=pacman.Pacman(200,479, "steven.jpg", 2)
                         #self.pacman_sprite=pygame.sprite.Group(self.Pacman)
                         self.Pacman.image=pygame.image.load("assets/steven.jpg")
                         self.Pacman.image = pygame.transform.scale(self. Pacman.image, (15,15))
                         self.Pacman.choose_list=2
                         self.Pacman.choose_img()
                         self.startGameLoop()
                 
            img = pygame.image.load('assets/logo.png')
            img=pygame.transform.scale(img, (500,100))
            red_rect=pygame.image.load("assets/red-rect.png")
            red_rect=pygame.transform.scale(red_rect, (200,100))
            map_pic=pygame.image.load("assets/opening -pic.jpg")
            map_pic=pygame.transform.scale(map_pic, (250,250))


            left1 = pygame.font.SysFont("Times New Roman", 25)
            left_mode_top=left1.render('Press Left Key ', False, (0, 0, 0))
            left_mode_bottom=left1.render("For Regular Mode", False, (0,0,0))


            
            right1 = pygame.font.SysFont("Times New Roman", 25)
            right_mode_top=right1.render('Press Right Key ', False, (0, 0, 0))
            right_mode_bottom=right1.render("For CS110 mode", False, (0,0,0))
            
            pacman=pygame.image.load("assets/pacman-home.png")
            pacman=pygame.transform.scale(pacman, (150,150))
            dots=pygame.image.load("assets/bigdot.png")
            #black_rect=pygame.image.load("assets/black-rect.png")
            #black_rect=pygame.transform.scale(black_rect, (150,150))
            
            high_score=right1.render("Current High Score: "+ self.high_score, False, (250,250,250))
            beat_it=right1.render("Can you beat it?", False, (250,250,250))

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(img,(245,0))
            self.screen.blit(red_rect,(150,450))
            self.screen.blit(red_rect,(650,450))

            self.screen.blit(left_mode_top, (180,460))
            self.screen.blit(left_mode_bottom, (160,490))
            self.screen.blit(right_mode_top, (672,460))
            self.screen.blit(right_mode_bottom, (665,490))
            self.screen.blit(map_pic, (370,400))
            self.screen.blit(pacman,(290,190))
            self.screen.blit(high_score, (340,110))
            self.screen.blit(beat_it, (387,150))
            x_val=490
            for i in range(3):
                self.screen.blit(dots, (x_val,260))
                x_val+=50
            
            #pacman_home_sprite=pygame.sprite.Group(pacman)
            #pacman_rect = pacman.get_rect()
            #rect.x = 290
            #rect.y = 150
            #speed = 1
            #for i in range(300):
                
             #   self.screen.blit(pacman_home_sprite,(rect.x, rect.y))
             #   rect.x+=speed
                

            #pacman_x=290
            #for i in range(3):
             #    self.screen.blit(pacman,(pacman_x, 150))
              #   self.screen.blit(black_rect, (pacman_x,150))
               #  pacman_x+=50
              

            pygame.display.flip()    


    def startGameLoop(self):
        while True:
            self.background.fill((0, 0, 0))
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.ready=True
                    begin_sound=pygame.mixer.Sound("assets/pacman_beginning.wav") 
                    begin_sound.play(0)  
                    if self.timer==True: 
                        pygame.time.delay(5000)           
                        self.timer=False
                        self.gameLoop()

            self.score_font=pygame.font.SysFont("Times New Roman", 30)
            start=self.score_font.render("Press any key to start!", False, (250,250,250))
            ready_font=pygame.font.SysFont("Times New Roman", 50)
            ready=ready_font.render("Ready?", False, (250,250,250))
            directions_rect=pygame.image.load('assets/white-rounded.png')
            directions_rect=pygame.transform.scale(directions_rect, (400, 200))
            directions=self.score_font.render("Directions:", False, (0,0,0))
            arrows=self.score_font.render("Use the arrow keys to move", False, (0,0,0))
            collect_dots=self.score_font.render("Collect all the dots", False, (0,0,0))
            no_ghosts=self.score_font.render("Don't get eaten by a ghost!", False, (0,0,0))

            
            
            self.screen.blit(self.background, (0, 0))

            self.dot_sprites.draw(self.screen)
            self.node_sprites.draw(self.screen)
            self.wall_sprites.draw(self.screen)
            self.ghost_sprite.draw(self.screen)
            self.Ghost.test_tiles.draw(self.screen)
            self.pacman_sprite.draw(self.screen)
            
            self.screen.blit(start, (80,0))
            self.screen.blit(ready,(150,550))
            self.screen.blit(directions_rect, (500,200))
            self.screen.blit(directions, (640,220))
            self.screen.blit(arrows, (540, 270))
            self.screen.blit(collect_dots, (540, 310))
            self.screen.blit(no_ghosts, (540, 350))


    

            pygame.display.flip()
 
    def gameLoop(self):
        #pygame.event.wait()
        while True:
            #if self.mode==1:
                #self.Pacman.image=assets/steven.jpg
                 #self.Pacman.choose_img==Steven
                 #self.Pacman.image=self.Pacman.rotated_list[0]
             #   self.Pacman.choose_img("1")
                 #self.Pacman.image=self.Pacman.rotated_list[0]
            #else:
             #   self.Pacman.choose_img("2")
                #self.Pacman.image=self.Pacman.rotated_list[0]
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
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_DOWN and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnDown()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                    elif event.key == pygame.K_RIGHT and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnRight()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_LEFT and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnLeft()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self. Pacman.image, (15,15))
                        
                    if event.key == pygame.K_UP and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 3:
                        self.Pacman.turnUp()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_DOWN and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 1:
                        self.Pacman.turnDown()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_RIGHT and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 2:
                        self.Pacman.turnRight()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_LEFT and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 0:
                        self.Pacman.turnLeft()
                        self.Pacman.speed = 1
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                     
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
                    self.wait_time=0  
 
            if self.Ghost.nodeCollide(self.node_sprites):

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
                
            #pygame.event.wait()
            #if self.noDelay:        
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

            self.dot_collide = self.Pacman.dotCollide(self.dot_sprites)
            self.big_dot_collide= self.Pacman.bigDotCollide(self.big_dot_sprites)
            if self.dot_collide[0]:
                self.dot_sprites.remove(self.dot_collide[1])
                self.current_score+=10
                #if self.dot_collide[1].state=="D":
                 #  self.current_score+=20               
            if (self.current_score)>(int(self.high_score)):
                self.high_score=self.current_score
                self.high_score_file=open("assets/highScore.txt", "w")
                self.high_score_file.write(str(self.high_score))
                self.high_score_file.close()

            if self.big_dot_collide[0]:
                self.dot_sprites.remove(self.dot_collide[1]) 
                self.current_score+=20   
                begin_sound=pygame.mixer.Sound("assets/pacman_chomp.wav") 
                #begin_sound.set_volume(.2)
                begin_sound.play(0) 
                            
                        
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



            #Scoreboard
            scoreboard=pygame.image.load('assets/white-rounded.png')
            scoreboard=pygame.transform.scale(scoreboard, (400, 200))
            score_title_font=pygame.font.SysFont("Times New Roman", 40)
            score_title_font.set_underline(1)
            score_title=score_title_font.render("Scoreboard", False, (0,0,0))
            #self.score_font=pygame.font.SysFont("Times New Roman", 30)
            ###ADD SCORE
            current_score=self.score_font.render("Current Score: " +str(self.current_score) , False, (0,0,0))
            high_score=self.score_font.render("High Score: "+str(self.high_score) , False, (0,0,0))
            
            #Lives
            life=pygame.image.load("assets/pacman1.png")
            life=pygame.transform.scale(life, (30,30))
            lives=self.score_font.render("Lives", False, (250,250,250))

            start=self.score_font.render("Press any key to start!", False, (250,250,250))
            ready_font=pygame.font.SysFont("Times New Roman", 50)
            #self.ready=ready_font.render("Ready?", False, (250,250,250))
                    
                   
            self.screen.blit(self.background, (0, 0))
            self.big_dot_sprites.draw(self.screen)
            self.dot_sprites.draw(self.screen)            
            self.node_sprites.draw(self.screen)
            self.wall_sprites.draw(self.screen)
            self.ghost_sprite.draw(self.screen)
            self.Ghost.test_tiles.draw(self.screen)
            self.pacman_sprite.draw(self.screen)
            
            

            
            self.screen.blit(scoreboard, (500,200))
            self.screen.blit(score_title,(605,215))
            self.screen.blit(current_score, (520, 270))
            self.screen.blit(high_score, (520, 310))
 
            #self.screen.blit(start, (80,0))
            
            self.screen.blit(lives, (175,510))
           # self.screen.blit(ready,(630,0))
            
            x_value=137
            for i in range(3):
                self.screen.blit(life, (x_value, 560))
                x_value+=50
            
            pygame.display.flip()  


    def endScreen(self):
        while True:
            self.background.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.startMenu()
            
            game_over=pygame.image.load("assets/game-over.png")
            game_over=pygame.transform.scale(game_over, (500,400))

            final_score_font=pygame.font.SysFont("Times New Roman", 35)
            final_score=final_score_font.render("Your final score is: " + str(self.current_score), False, (250,250,250))
            white_rect=pygame.image.load("assets/white-rounded.png")
            white_rect=pygame.transform.scale(white_rect, (300,100))
            play_again1=final_score_font.render("Press any key to ", False, (0,0,0))
            play_again2=final_score_font.render("play again", False, (0,0,0))
            


            self.screen.blit(self.background, (0,0))
            self.screen.blit(game_over, (250,0))
            self.screen.blit(final_score, (350, 350))
            
            self.screen.blit(white_rect, (350,450))
            self.screen.blit(play_again1, (385, 460))
            self.screen.blit(play_again2, (420, 495))

            pygame.display.flip() 

  


    def screen_img(self):
        while self.state!="End":
            if self.state=="Start":
                #self.startMenu()
                self.endScreen()
            elif self.state=="Game":
                self.gameLoop()





def main():
    main_window = Controller() 
    main_window.screen_img()  
     
    #main_window = Controller() 
    #main_window.startMenu()
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

