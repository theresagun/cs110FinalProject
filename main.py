import pygame
import pacman

WHITE = (255, 255, 255)

#initialise pygame engine/libray
pygame.init()

#The size(in pixels) of the window
size = (700, 500)
#Creating the window in which the game is played
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pacman')

#Boolean which keeps the game going or stops it
carryOn = True

#used to control how fast screen updates
clock = pygame.time.Clock()

character = pacman.Pacman()

while carryOn:
    #gets the users events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryon = False
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #character.moveSurface(screen)
    
    #Calls pacman's moveSurface() method which adds 1 to his x value
    character.moveSurface(screen)

    #fills the screen in white and clears the previous frame's canvas
    screen.fill(WHITE)
    
    #Places pacman onto the screen using the blit pygame method
    character.getSurface(screen)

    #updates screen
    pygame.display.flip()

#limits to 60 fps
    clock.tick(60)

pygame.quit()