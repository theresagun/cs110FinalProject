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
        self.mode=1
        self.timer=True
        self.ready=False
        self.small_dot_amt=181
        self.big_dot_amt=4
        self.clock=pygame.time.Clock()
        self.time=self.clock.tick()
        
        self.Pacman=pacman.Pacman(200,479, "pacman1.png", 2)
        
        self.Ghost = ghosts.Ghost(315, 315, 'blueghost.png', 1)

        self.current_score=0
 
        self.high_score_file=open("assets/highScore.txt", "r")
        self.high_score_json=self.high_score_file.readline().strip()
        self.high_score_dict=json.loads(self.high_score_json)
        self.high_score=self.high_score_dict["High Score"]
        self.high_score_file.close()
        
        
        #self.high_score_file=open("assets/highScore.txt", "r")
        #self.high_score=self.high_score_file.readline().strip()

        self.create_map=maps.Map((300,300), 15)
        
        #self.sprites=pygame.sprite.Group((self.map_background)+ (self.Pacman))
        

        self.map_background=maps.Map.load_map(self.create_map)
        self.wall_sprites = pygame.sprite.Group(self.map_background[0])
        self.dot_sprites = pygame.sprite.Group(self.map_background[1])
        #self.dot_sprites_reset=pygame.sprite.Group(self.map_background[1])
        self.node_sprites = pygame.sprite.Group(self.map_background[2])
        self.big_dot_sprites=pygame.sprite.Group(self.map_background[3])
        self.ghost_sprite=pygame.sprite.Group(self.map_background[5])
        self.Pacman=self.map_background[4]
        self.pacman_sprite=pygame.sprite.Group(self.Pacman)



    def startMenu(self):
        while True:
            self.background.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                         self.mode=1                         
                         #self.Pacman.image=pygame.image.load("assets/pacman1.png")
                         self.Pacman.choose_list=1
                         self.Pacman.choose_img()
                         self.startGameLoop()
                     if event.key == pygame.K_RIGHT:
                         self.mode=2
                         self.Pacman.image=pygame.image.load("assets/steven.jpg")
                         self.Pacman.image = pygame.transform.scale(self. Pacman.image, (15,15))
                         self.Pacman.choose_list=2
                         self.Pacman.choose_img()
                         self.startGameLoop()
            
            # Creating logo, red rectangles to hold words,and map image     
            logo = pygame.image.load('assets/logo.png').convert_alpha()
            logo=pygame.transform.scale(logo, (500,100)).convert_alpha()
            red_rect=pygame.image.load("assets/red-rect.png").convert_alpha()
            red_rect=pygame.transform.scale(red_rect, (200,100)).convert_alpha()
            map_pic=pygame.image.load("assets/opening -pic.jpg").convert_alpha()
            map_pic=pygame.transform.scale(map_pic, (250,250)).convert_alpha()

            # Text for left box (regular mode)
            left1 = pygame.font.SysFont("Times New Roman", 25)
            left_mode_top=left1.render('Press Left Key ', False, (0, 0, 0))
            left_mode_bottom=left1.render("For Regular Mode", False, (0,0,0))


            # Text for right box (Cs110 mode)
            right1 = pygame.font.SysFont("Times New Roman", 25)
            right_mode_top=right1.render('Press Right Key ', False, (0, 0, 0))
            right_mode_bottom=right1.render("For CS110 mode", False, (0,0,0))
            
            # Create image of pacman and the dot
            pacman=pygame.image.load("assets/pacman-home.png").convert_alpha()
            pacman=pygame.transform.scale(pacman, (150,150)).convert_alpha()
            dots=pygame.image.load("assets/bigdot.png").convert_alpha()
            #black_rect=pygame.image.load("assets/black-rect.png")
            #black_rect=pygame.transform.scale(black_rect, (150,150))
            
            # Text for high score information
            high_score=right1.render("Current High Score: "+ str(self.high_score), False, (250,250,250))
            beat_it=right1.render("Can you beat it?", False, (250,250,250))

           
            self.screen.blit(self.background, (0, 0))
            # Putting logo, map, Pacman, and red rectangles on screen (all images)
            self.screen.blit(logo,(245,0))
            self.screen.blit(red_rect,(150,450))
            self.screen.blit(red_rect,(650,450))
            self.screen.blit(map_pic, (370,400))
            self.screen.blit(pacman,(290,190))

            #Putting all text on screen 
            self.screen.blit(left_mode_top, (180,460))
            self.screen.blit(left_mode_bottom, (160,490))
            self.screen.blit(right_mode_top, (672,460))
            self.screen.blit(right_mode_bottom, (665,490)) 
            self.screen.blit(high_score, (340,110))
            self.screen.blit(beat_it, (387,150))

            # Adding 3 dots on screen
            x_val=490
            for i in range(3):
                self.screen.blit(dots, (x_val,260))
                x_val+=50
            

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

            # Ready and click any key to start text
            self.score_font=pygame.font.SysFont("Times New Roman", 30)
            start=self.score_font.render("Press any key to start!", False, (250,250,250))
            ready_font=pygame.font.SysFont("Times New Roman", 50)
            ready=ready_font.render("Ready?", False, (250,250,250))

            # Rectangle image to put directions in and the directions text
            directions_rect=pygame.image.load('assets/white-rounded.png').convert_alpha()
            directions_rect=pygame.transform.scale(directions_rect, (400, 200)).convert_alpha()
            directions=self.score_font.render("Directions:", False, (0,0,0))
            arrows=self.score_font.render("Use the arrow keys to move", False, (0,0,0))
            collect_dots=self.score_font.render("Collect all the dots", False, (0,0,0))
            no_ghosts=self.score_font.render("Don't get eaten by a ghost!", False, (0,0,0))

            
            
            self.screen.blit(self.background, (0, 0))
 
            # Draws all sprites on screen
            self.dot_sprites.draw(self.screen)
            
            self.wall_sprites.draw(self.screen)
            self.ghost_sprite.draw(self.screen)
            self.big_dot_sprites.draw(self.screen)
            self.pacman_sprite.draw(self.screen)

            # Puts all text/image objects on screen
            self.screen.blit(start, (80,0))
            self.screen.blit(ready,(150,550))
            self.screen.blit(directions_rect, (500,200))
            self.screen.blit(directions, (640,220))
            self.screen.blit(arrows, (540, 270))
            self.screen.blit(collect_dots, (540, 310))
            self.screen.blit(no_ghosts, (540, 350))


    

            pygame.display.flip()
 
    def gameLoop(self):        
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
                        self.Pacman.speed = 3
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_DOWN and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnDown()
                        self.Pacman.speed = 3
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                    elif event.key == pygame.K_RIGHT and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnRight()
                        self.Pacman.speed = 3
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self.Pacman.image, (15,15))
                        
                    elif event.key == pygame.K_LEFT and self.Pacman.canMove(self.wall_sprites) and self.dot_is_colliding:
                        self.Pacman.rect.centerx = self.colliding_dot.rect.centerx
                        self.Pacman.rect.centery = self.colliding_dot.rect.centery
                        self.Pacman.turnLeft()
                        self.Pacman.speed = 3
                        self.Pacman.image=self.Pacman.rotated_img
                        self.Pacman.image = pygame.transform.scale(self. Pacman.image, (15,15))
                        
                    if event.key == pygame.K_UP and self.Pacman.canMove(self.wall_sprites) and self.Pacman.direction == 3:
                        self.Pacman.turnUp()
                        self.Pacman.speed = 3
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
            
            for ghost in self.ghost_sprite:
                ghost.update(self.node_sprites, self.wall_sprites)
        
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
                self.small_dot_amt-=1
                begin_sound=pygame.mixer.Sound("assets/pacman_chomp.wav") 
                begin_sound.play(0) 
                #if self.dot_collide[1].state=="D":
                 #  self.current_score+=20               
            if (self.current_score)>(int(self.high_score)):
                self.high_score=self.current_score
                self.high_score_dict["High Score"]=self.high_score
                self.high_score_file=open("assets/highScore.txt", "w")
                self.high_score_make_json=json.dumps(self.high_score_dict)
                self.high_score_file.write(self.high_score_make_json)
                self.high_score_file.close()

            if self.big_dot_collide[0]:

                self.time=self.clock.tick()
                #self.big_dot_sprites=big_dot_sprites
                #big_dot_sprites.remove(self.big_dot_collide[1]) 
                self.big_dot_sprites.remove(self.big_dot_collide[1]) 
                self.current_score+=20
                self.big_dot_amt-=1 
                begin_sound=pygame.mixer.Sound("assets/pacman_chomp.wav") 
                begin_sound.play(0) 

                if self.mode==1: 
                    self.inverted_ghost=pygame.image.load("assets/ghost-eaten.png").convert_alpha()
                    self.Ghost.image=pygame.transform.scale(self.inverted_ghost, (15,15)).convert_alpha()
                #clock.tick()
                #time_passed=clock.get_time()
            #if time_passed==(time-1000) or time_passed==(time+1000):
             #   self.original_image=pygame.image.load("assets/blueghost.png").convert_alpha()
              #  self.Ghost.image= pygame.transform.scale(self.image, (15,15))
            if self.clock.tick()>=self.time+4000:            
                self.original_image=pygame.image.load("assets/blueghost.png").convert_alpha()
                self.Ghost.image= pygame.transform.scale(self.original_image, (15,15))   
                #elif self.mode==2:
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")

                    
                
            if self.small_dot_amt==0 and self.big_dot_amt==0:
                self.Pacman.rect.x=200   
                self.Pacman.rect.y=479
                self.reset()

                
                

                #if score.Score.lives==0
		    #GAME OVER



            #Scoreboard
            scoreboard=pygame.image.load('assets/white-rounded.png').convert_alpha()
            scoreboard=pygame.transform.scale(scoreboard, (400, 200)).convert_alpha()
            score_title_font=pygame.font.SysFont("Times New Roman", 40)
            score_title_font.set_underline(1)
            score_title=score_title_font.render("Scoreboard", False, (0,0,0))            
            current_score=self.score_font.render("Current Score: " +str(self.current_score) , False, (0,0,0))
            high_score=self.score_font.render("High Score: "+str(self.high_score) , False, (0,0,0))
                  
            #Lives
            life=pygame.image.load("assets/pacman1.png").convert_alpha()
            life=pygame.transform.scale(life, (30,30)).convert_alpha()
            lives=self.score_font.render("Lives", False, (250,250,250))
               
            self.Pacman.outsideMap()


            #Black Rect for next to map
            black_rect=pygame.image.load("assets/black-rect.png").convert_alpha()
            black_rect=pygame.transform.scale(black_rect,(15,15)).convert_alpha()
                             
                   
            self.screen.blit(self.background, (0, 0))
            #Draw all sprites on screen
            self.big_dot_sprites.draw(self.screen)
            self.dot_sprites.draw(self.screen)            
            
            self.wall_sprites.draw(self.screen)
            self.ghost_sprite.draw(self.screen)
            
            self.pacman_sprite.draw(self.screen)
            
            #Put all images/text on screen       
            self.screen.blit(scoreboard, (500,200))
            self.screen.blit(score_title,(605,215))
            self.screen.blit(current_score, (520, 270))
            self.screen.blit(high_score, (520, 310))
            self.screen.blit(lives, (175,510))

            #Puts 3 pacman image on screen, each representing a life
            x_value=137
            for i in range(3):
                self.screen.blit(life, (x_value, 560))
                x_value+=50
            #Put Black Rect on map
            self.screen.blit(black_rect, (420, 255))

            
            
            pygame.display.flip()  


    def reset(self):
        self.small_dot_amt=181
        self.big_dot_amt=4
        self.dot_sprites = pygame.sprite.Group(self.map_background[1])
        self.big_dot_sprites=pygame.sprite.Group(self.map_background[3])
        self.Pacman.speed+=10
        self.Pacman.direction=0
        self.gameLoop()


    def endScreen(self):
        while True:
            self.background.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.startMenu()

            #Game Over Logo created            
            game_over=pygame.image.load("assets/game-over.png").convert_alpha()
            game_over=pygame.transform.scale(game_over, (500,400)).convert_alpha()

            #Final score text
            final_score_font=pygame.font.SysFont("Times New Roman", 35)
            final_score=final_score_font.render("Your final score is: " + str(self.current_score), False, (250,250,250))
            #Play again background rect and text
            white_rect=pygame.image.load("assets/white-rounded.png").convert_alpha()
            white_rect=pygame.transform.scale(white_rect, (300,100)).convert_alpha()
            play_again1=final_score_font.render("Press any key to ", False, (0,0,0))
            play_again2=final_score_font.render("play again", False, (0,0,0))
            

            #Put all images/text on screen
            self.screen.blit(self.background, (0,0))
            self.screen.blit(game_over, (250,0))
            self.screen.blit(final_score, (350, 350))
            self.screen.blit(white_rect, (350,450))
            self.screen.blit(play_again1, (385, 460))
            self.screen.blit(play_again2, (420, 495))

            pygame.display.flip() 

  
            
def main():
    main_window = Controller() 
    #main_window.screen_img()  
    main_window.endScreen()
    #main_window = Controller() 
    #main_window.startMenu()
main()		
		
