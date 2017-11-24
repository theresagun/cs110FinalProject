import pygame
import pacman
import maps
import sys


class Controller:
    def __init__ (self, width=960, height=540):
        pygame.init()
        self.width=width
        self.height=height
        self.screen=pygame.display.set_mode((self.width, self.height))
        self.caption=pygame.display.set_caption('Pacman')
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.Pacman=pacman.Pacman(0,0, "red-square.png" , 1)
     
        #self.screen.blit(self.Pacman, (480,520))
        #self.Pacman.getSurface()
        self.create_map=maps.Map((100,100), 10)
        self.map_background=maps.Map.load_map(self.create_map)
        #self.sprites=pygame.sprite.Group((self.map_background)+ (self.Pacman))
        #for walls in self.map_background: 	
         #   self.screen.blit(walls)

    def mainLoop(self):
        while True:
            self.background.fill((250, 250, 250))
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type == pygame.K_DOWN:
                    self.Pacman.turnDown()
                if event.type == pygame.K_UP:
                    self.Pacman.turnUp
                if event.type == pygame.K_LEFT:
                    self.Pacman.turnLeft
                if event.type == pygame.K_RIGHT:
            	    self.Pacman.turnRight
                
                #if score.Score.lives==0
		    #GAME OVER

               

            #self.sprites.draw(self.screen)
            pygame.display.flip()    

def main():
    main_window = Controller()
    main_window.mainLoop()
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
