import pygame
import wall1
import dot
import node
import pacman
import ghosts
import random


class Map:
    def __init__(self, display_size, tile_size):
        '''
        Initializes a map object with attributes: map_file, display_size, tile_size, tile_list, wall_list, dot_list, big_dot_list, node_list.
        '''
        #self.map_file is a text file with a bunch of 1's and 0's based on what we want in that position.
        self.map_file = open('assets/map.txt', 'r')

        #self.display_size is the size of the display, this may not need to be used in this class
        self.display_size = display_size
    
        #self.tile_size is the size of the tile in pixels that we want. We can determine this
        #based on how big in pixels we want the map to be. The size
        #of the tiles are 15x15 and the size of the map is 28x36
        self.tile_size = tile_size

    def load_map(self):
        '''
        Reads a text file with directions on how to create the map.
        Loads in image files respectively.
        '''
        #this reads the file and creates a list of the certain sprites based on the letter.
        #self.tile_list looks something like -> [['1', '1', '1',...], ['1', '0', '0',...], [...], ...]
        self.tile_list = []
        for line in self.map_file:
            self.tile_list.append(list(line.rstrip()))
        self.map_file.close()

        #reads the self.tile_list, the 'row' variable is the index of the current list iteration,
        #the 'col' is index of each character in the current 'row'. This loops through each
        #tile in the 2D list and then creates a 'Wall' sprite in the correct spot.
        #it then returns each list so we can make it a sprite group and blit it to the screen.
        #list of walls
        self.wall_list = []
        #list of small dots
        self.dot_list = []
        #list of big dots
        self.big_dot_list=[]
        #list of nodes at each intersection
        self.node_list = []
        #list of ghosts
        self.ghost_list = []
        for row in range(len(self.tile_list)):
            for col in range(len(self.tile_list[row])):
                if self.tile_list[row][col] in ['h', 'v', 'w', 'x', 'y', 'z']:
                    self.wall_list.append(wall1.Wall(col*self.tile_size, row*self.tile_size, 'normal-rect.png'))
                elif self.tile_list[row][col] == 'd':
                    self.dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'dot.png', 'd'))
                elif self.tile_list[row][col] == 'D':
                    self.big_dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'bigdot.png', 'D'))
                elif self.tile_list[row][col] == 'n':
                    self.node_list.append(node.Node(col*self.tile_size, row*self.tile_size, 'red-square.png'))
                    self.dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'dot.png', 'd'))
                elif self.tile_list[row][col] == 'P':
                    self.pacman_x=col*self.tile_size
                    self.pacman_y=row*self.tile_size
                    self.pacman_tile = pacman.Pacman(col*self.tile_size, row*self.tile_size, "pacman1.png", 0)
                elif self.tile_list[row][col] == 'r':
                    self.ghost_list.append(ghosts.Ghost(col*self.tile_size, row*self.tile_size, 'redghost.png', random.choice([0,2]), "red", 2))
                    self.ghost_rx=col*self.tile_size
                    self.ghost_ry=row*self.tile_size
                    
                    self.dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'dot.png', 'd'))
                elif self.tile_list[row][col] == 'p':
                    self.ghost_list.append(ghosts.Ghost(col*self.tile_size, row*self.tile_size, 'pinkghost.png', 1, "pink", 1))
                    self.ghost_px=col*self.tile_size
                    self.ghost_py=row*self.tile_size
                elif self.tile_list[row][col] == 'b':
                    self.ghost_list.append(ghosts.Ghost(col*self.tile_size, row*self.tile_size, 'blueghost.png', 1, "blue", 1))
                    self.ghost_bx=col*self.tile_size
                    self.ghost_by=row*self.tile_size
    
                elif self.tile_list[row][col] == 'o':
                    self.ghost_list.append(ghosts.Ghost(col*self.tile_size, row*self.tile_size, 'orange-ghost.png', 1, "orange", 1))
                    self.ghost_ox=col*self.tile_size
                    self.ghost_oy=row*self.tile_size
                elif self.tile_list[row][col] == 'g':
                    self.wall_list.append(wall1.Wall(col*self.tile_size, row*self.tile_size, 'black-grey.png'))
                    
        return self.wall_list, self.dot_list, self.node_list, self.big_dot_list, self.pacman_tile, self.ghost_list

