import os
import sys
import time
import pyautogui
import pydirectinput
from PIL import Image
from Ghost import *
from utils import *

class Board:
    def __init__(self):
        self.blinky = Blinky()
        self.pinky = Pinky()
        self.inky = Inky()
        self.clyde = Clyde()
        self.ghosts = [self.blinky, self.pinky, self.inky, self.clyde]
        #PACMAN DOES NOT HAVE ACCESS TO PORTAL ON THIS BOARD
        self.state = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                      [2, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 2],
                      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        #STATE INCLUDING CONSUMED PELLETS
        self.pelletState = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                            [1, 5, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 5, 1],
                            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 0, 1, 1, 1, 8, 1, 8, 1, 1, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 8, 8, 8, 8, 8, 8, 8, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 8, 1, 1, 1, 1, 1, 8, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 8, 1, 1, 1, 1, 1, 8, 1, 0, 1, 1, 1, 1, 1],
                            [2, 8, 8, 8, 1, 0, 8, 8, 1, 1, 1, 1, 1, 8, 8, 0, 1, 8, 8, 8, 2],
                            [1, 1, 1, 1, 1, 0, 1, 8, 1, 1, 1, 1, 1, 8, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 8, 8, 8, 8, 8, 8, 8, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 8, 1, 1, 1, 1, 1, 8, 1, 0, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 0, 1, 8, 1, 1, 1, 1, 1, 8, 1, 0, 1, 1, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                            [1, 5, 0, 0, 1, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 1, 0, 0, 5, 1],
                            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
                            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    def update(self):       
        print("Updating board...")
        self.updatePellets()
        print("-----------------")
        for item in self.ghosts:
            item.update()
            item.printDetails()
        print("-----------------")

    def updatePellets(self):
        im = pyautogui.screenshot(region=(505, 150, 620, 815))
        x = 22      
        y = 793       
        init = [x, y]
        for i in range(25):
            #print("Row: " + str(25 - i))
            for j in range(19):
                tmp = (init[0], init[1])
                coord = convertPosToCoord((tmp[0] + 505, tmp[1] + 150))
                pix = im.getpixel(tmp)
                #locates pellets
                if(not matchPixels(pix, (237, 155, 45)) and self.pelletState[int(coord[1])][int(coord[0])] == 0):
                    if(matchPixels(pix, (0, 0, 0))):   
                        self.pelletState[26 - i][j + 1] = 8
                        #print("CRONCH! " + str(coord))
                #locates ghosts
                if(matchPixels(pix, (126, 3, 1))):
                    self.blinky.coordinate = coord
                    #print("Blinky boolin at: " + str(coord))
                if(matchPixels(pix, (237, 186, 255))):
                    self.pinky.coordinate = coord
                    #print("Pinky vibing at: " + str(coord))
                if(matchPixels(pix, (99, 180, 255))):
                    self.inky.coordinate = coord
                    #print("Inky j chillin at: " + str(coord))
                if(matchPixels(pix, (147, 77, 1))):
                    self.clyde.coordinate = coord
                    #print("Clyde's dumbass at: " + str(coord))
                init[0] += 32 
            init[0] = 22
            init[1] -= 32
    
    def weighQuadrants(self):
        quads = [0, 0, 0, 0]
        #top left
        for i in range(1, 13):
            for j in range(1, 10):
                if(self.pelletState[i][j] == 0):
                    quads[0] += 1
        #top right
        for i in range(1, 13):
            for j in range(11, 20):
                if(self.pelletState[i][j] == 0):
                    quads[1] += 1
        #bottom left
        for i in range(14, 26):
            for j in range(1, 10):
                if(self.pelletState[i][j] == 0):
                    quads[2] += 1
        #bottom right
        for i in range(14, 13):
            for j in range(11, 20):
                if(self.pelletState[i][j] == 0):
                    quads[3] += 1
        return quads 


    