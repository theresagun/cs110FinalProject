import pygame
import pacman


class Controller:
    def __init__ (self, width=960, height=540):
	pygame.init()
	self.width=width
	self.height=height
	self.screen=pygame.display.set_mode((self.width, self.height))
	#self.background=??
	self.Pacman=pacman.Pacman(5,(480,520),self.screen)
	self.Pacman.pacman.getSurface()
	#self.ghost1=ghost.Ghost(<waiting for ghost class to be created>)
        #self.ghost2=ghost.Ghost(<waiting for ghost class to be created>)
        #self.ghost3=ghost.Ghost(<waiting for ghost class to be created>)
        #self.ghost4=ghost.Ghost(<waiting for ghost class to be created>)

	self.map_background=map.load_map()
	#map_sprites=pygame.sprite.Group(self.map_background+self.Pacman)
        for walls in self.map_background: 	
            self.screen.blit(walls)
	


    def main():
	while True:
	    for event in pygame.event.get():
		if event.type==pygame.QUIT:
		    sys.exit()
		if event.type == pygame.K_DOWN:
                    character.turnSurface('SOUTH')
		if event.type == pygame.K_UP:
                    character.turnSurface('NORTH')
		if event.type == pygame.K_LEFT:
                    character.turnSurface('WEST')
		if event.type == pygame.K_RIGHT:
            	    character.turnSurface('EAST')
                
		#if score.Score.lives==0
		    #GAME OVER
                

		
		
	







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
