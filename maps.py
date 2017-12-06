import pygame
import wall1
import dot
import node


class Map:
    def __init__(self, display_size, tile_size):
        #self.map_file is a text file with a bunch of 1's and 0's based on what we want in that position.
        self.map_file = open('assets/map.txt', 'r')

        #self.display_size is the size of the display, this may not need to be used in this class
        self.display_size = display_size
    
        #self.tile_size is the size of the tile in pixels that we want. We can determine this
        #based on how big in pixels we want the map to be. As of right now, if the size of the map is 100x100
        #pixels, and we want 10 tiles, the size of the tile will be 10x10 in pixels
        self.tile_size = tile_size

    def load_map(self):
        '''
        Reads a text file with directions on how to create the map.
        Loads in image files respectively.
        '''
        #this reads the file and creates a list of 1's and 0's based on each line of the file
        #self.tile_list looks like -> [['1', '1', '1',...], ['1', '0', '0',...], [...], ...]
        self.tile_list = []
        for line in self.map_file:
            self.tile_list.append(list(line.rstrip()))
        self.map_file.close()

        #reads the self.tile_list, the 'row' variable is the index of the current list iteration,
        #the 'col' is index of each character in the current 'row'. This loops through each
        #tile in the 2D list and then creates a 'Wall' sprite in the correct spot.
        #it then returns the wall_list so we can make it a sprite group and blit it to the screen.
        self.wall_list = []
        self.dot_list = []
        self.big_dot_list=[]
        self.node_list = []
        self.floor_list = []
        for row in range(len(self.tile_list)):
            for col in range(len(self.tile_list[row])):
                if self.tile_list[row][col] in ['h', 'v', 'w', 'x', 'y', 'z']:
                    self.wall_list.append(wall1.Wall(col*self.tile_size, row*self.tile_size, 'normal-rect.png'))
                elif self.tile_list[row][col] in ['d','P']:
                    self.dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'dot.png', 'd'))
                elif self.tile_list[row][col] in ['D']:
                    self.big_dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'bigdot.png', 'D'))
                #elif self.tile_list[row][col] == 'w':
                    #self.wall_list.append(wall1.Wall(col*self.tile_size, row*self.tile_size, 'rounded-rect.png'))
                elif self.tile_list[row][col] == 'n':
                    self.node_list.append(node.Node(col*self.tile_size, row*self.tile_size, 'red-square.png'))
                    self.dot_list.append(dot.Dot(col*self.tile_size, row*self.tile_size, 'dot.png', 'd'))
                    
        return self.wall_list, self.dot_list, self.node_list, self.big_dot_list
