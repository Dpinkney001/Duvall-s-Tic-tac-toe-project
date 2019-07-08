# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 05:06:39 2018

@author: Duvall Pinkney
         Duvall.Pinkney@gmail.com
"""

#Duvall Pinkney
#12/8/2018


from turtle  import *

#    #-------------------------initialize values-------------------------
 #create gamplay loop with win conditions
def main():
        
    #drawGrid
    #initialize ninja turtle
    win = Screen()
    ninja = Turtle()
    ninja.shape('turtle')
    win.title('Duvall version of TIC TAC TOE GAME')
    
    
    # draw grid-------300 x 300 box
    # 100 pixels x 100 pixels box with center at (x -50,y-50) pixels
    #point(0,0) starting
    ninja.up()
    ninja.forward(150)
    ninja.left(90)
    ninja.down()
    ninja.forward(150)
    
    ninja.left(90)
    #point(150,150) pixels
    
    ninja.forward(300)
    #point(-150,150)
    
    ninja.left(90)
    ninja.forward(300)
    #point(-150,-150)
    ninja.left(90)
    ninja.forward(300)
    #point(150,-150)
    ninja.left(90)
    ninja.forward(300)
    #point(150,150)
    
    ninja.up()
    ninja.left(90)
    ninja.forward(100)
    #point(50,150)
    ninja.left(90)
    ninja.down()
    ninja.forward(300)
    #point(50,-150)
    ninja.right(90)
    ninja.up()
    ninja.forward(100)
    #point(-50,-150)
    ninja.right(90)
    ninja.down()
    ninja.forward(300)
    #point(50,150)
    ninja.up()
    ninja.left(90)
    ninja.forward(100)
    ninja.left(90)
    ninja.forward(100)
    ninja.left(90)
    ninja.down()
    ninja.forward(300)
    ninja.up()
    ninja.right(90)
    ninja.forward(100)
    ninja.right(90)
    ninja.down()
    ninja.forward(300)
    #enlarge value or X and O and print fill in grid color with blue or 
    #red X or O
    #int numberOfTurns = 0; 
    
    
    x = 0
    y = 0
    numberOfTurns = 0
    topLeftGrid = ""
    topCenterGrid = ""
    topRightGrid = ""
    centerLeftGrid = ""
    centerGrid = ""
    centerRightGrid = ""
    bottomLeftGrid = ""
    bottomCenterGrid = ""
    bottomRightGrid = ""
    
    
    while (numberOfTurns <= 9):
        #player X always goes first
        print("player X always goes first")
        value = "X";
        print("Chose a grid for X")
        
        numberOfTurns = numberOfTurns + 1;
        x,y = ninja.onclick(ninja.goto(x),ninja.goto(y))
    
        # if user click within the box of center left go to the center of 
        # of the box and write value at the center
        if ((x >= -100 & x <= -50) & (y >= -50 & y <= 50)):
            ninja.goto(-100,0)
            ninja.write("X")
            centerLeftGrid = "X"
            
        # if user click within the box of Top left go to the top left of 
        # of the box and write value at the center of the region
        elif ((x >= -100 & x <= -50) & (y >= 50 & y <= 150)):
            ninja.goto(-100,100)
            ninja.write("X")
            topLeftGrid = "X"
            
        if (x + 50 <= 150 & x - 50 >= -150) & (y + 50 <= 150 & y - 50 >= -150):
            newX = x - x + 100
            newY = y - y + 100
            ninja.goto(newX,newY)
            ninja.write(value)
    
        # player "O" turn
        value = "O";
        #game victory conditions
        if (topLeftGrid & centerLeftGrid & bottomLeftGrid == "X"):
            print("player X wins")
            break
        elif (topLeftGrid & centerLeftGrid & bottomLeftGrid == "O"):
            print("player O wins")
            break
        elif (topCenterGrid & centerGrid & bottomCenterGrid == "X"):
            print("player X wins")
            break
        elif (topCenterGrid & centerGrid & bottomCenterGrid == "O"):
            print("player O wins")
            break
        elif (topRightGrid & centerRightGrid & bottomRightGrid == "X"):
            print("player X wins")
            break
        elif (topRightGrid & centerRightGrid & bottomRightGrid == "O"):
            print("player O wins")
            break
        elif (topLeftGrid & topCenterGrid & topRightGrid == "X"):
            print("player X wins")
            break
        elif (topLeftGrid & topCenterGrid & topRightGrid == "O"):
            print("player O wins")
            break
        elif (centerLeftGrid & centerGrid & centerRightGrid == "X"):
            print("player X wins")
            break
        elif (centerLeftGrid & centerGrid & centerRightGrid == "O"):
            print("player O wins")
            break
        elif (bottomLeftGrid & bottomCenterGrid & bottomRightGrid == "X"):
            print("player X wins")
            break
        elif (bottomLeftGrid & bottomCenterGrid & bottomRightGrid == "O"):
            print("player O wins")
            break
        elif (topLeftGrid & centerGrid & bottomRightGrid == "X"):
            print("player X wins")
            break
        elif (topLeftGrid & centerGrid & bottomRightGrid == "O"):
            print("player O wins")
            break
        elif ( topRightGrid & centerGrid & bottomLeftGrid == "X"):
            print("player X wins")
            break
        elif ( topRightGrid & centerGrid & bottomLeftGrid == "O"):
            print("player O wins")
            break
        else:
            print("it is a draw")
            break
        #get user input
   
        
        
        
        
    
#decide by random who goes first X or O

def onClickCommands():
    xClick = 0
    yClick = 0
    
    

   
# create X controls so that if grid is  filled you can not select it
def Xcontrols(xValue):
    xValue = this.xValue;
    value = xValue;
        #----------------In game controls/methods-------------------------------
    def topleft(value):
        xOutput = -100
        yOutput = 100
        ninja.goto(xOutput, yOutput)
        if (topLeftGrid == ""):
            ninja.write(value)
        elif (topLeftGrid == "O"):
            print("You can not write to this grid choose another")
            #insert function call to choosing a grid
        
        
        
        #object storing value for win conditions
        # X or O
        topLeftGrid = value
    
        
    def centerleft(value):
        xOutput = -100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerLeftGrid = value
        
    def bottomleft(value):
        xOutput = -100
        yOutput = -100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomLeftGrid = value
        
    def topcenter(value):    
        xOutput = 0
        yOutput = 100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        topCenterGrid = value
        
    def center(value):
        xOutput = 0
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerGrid = value
        
        
    def bottomcenter(value):
        xOutput = -100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomCenterGrid = value
        
    def topright(value):
        xOutput = 100
        yOutput = 100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        topRightGrid = value
        
        
    def centerright(value):
        xOutput = 100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerRightGrid = value
        
    def bottomright(value):
        xOutput = 100
        yOutput = -100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomRightGrid = value


#create O controls so that if grid is filled you can not select it
def Ocontrols( oValue ):
    oValue = this.oValue;
    value = oValue;
        #----------------In game controls/methods-------------------------------
    def topleft(value):
        xOutput = -100
        yOutput = 100
        ninja.goto(xOutput, yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        # X or O
        topLeftGrid = value
        
    def centerleft(value):
        xOutput = -100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerLeftGrid = value
        
    def bottomleft(value):
        xOutput = -100
        yOutput = -100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomLeftGrid = value
        
    def topcenter(value):    
        xOutput = 0
        yOutput = 100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        topCenterGrid = value
        
    def center(value):
        xOutput = 0
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerGrid = value
        
        
    def bottomcenter(value):
        xOutput = -100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomCenterGrid = value
        
    def topright(value):
        xOutput = 100
        yOutput = 100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        topRightGrid = value
        
        
    def centerright(value):
        xOutput = 100
        yOutput = 0
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        centerRightGrid = value
        
    def bottomright(value):
        xOutput = 100
        yOutput = -100
        ninja.goto(xOutput,yOutput)
        ninja.write(value)
        
        #object storing value for win conditions
        bottomRightGrid = value
        




#--------------------end grid construction---------------------------------


#coordinates of the center of each 100 x 100 grid
#----------------In game controls/methods-------------------------------
def topleft(value):
    xOutput = -100
    yOutput = 100
    ninja.goto(xOutput, yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    # X or O
    topLeftGrid = value
    
def centerleft(value):
    xOutput = -100
    yOutput = 0
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    centerLeftGrid = value
    
def bottomleft(value):
    xOutput = -100
    yOutput = -100
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    bottomLeftGrid = value
    
def topcenter(value):    
    xOutput = 0
    yOutput = 100
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    topCenterGrid = value
    
def center(value):
    xOutput = 0
    yOutput = 0
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    centerGrid = value
    
    
def bottomcenter(value):
    xOutput = -100
    yOutput = 0
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    bottomCenterGrid = value
    
def topright(value):
    xOutput = 100
    yOutput = 100
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    topRightGrid = value
    
    
def centerright(value):
    xOutput = 100
    yOutput = 0
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    centerRightGrid = value
    
def bottomright(value):
    xOutput = 100
    yOutput = -100
    ninja.goto(xOutput,yOutput)
    ninja.write(value)
    
    #object storing value for win conditions
    bottomRightGrid = value
        
        
        
        
        
    


main()