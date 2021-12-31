#imports
from matplotlib import pyplot
import numpy as np
import random
import board
from queue import PriorityQueue


class creator:


#This is the set up function, it will ask the user to determine the parameters of the grid. Users will enter the numbers in to the terminal and the system will use these values to create a grid.
    def setup(self):
        print("Welcome to the set up stage")
        self.gridHeight = int(input("\nHow high do you want the grid to be? "))
        self.gridWidth = int(input("\nHow wide do you want the grid to be? "))
        # start position
        self.robot_x = 0
        self.robot_y = 0
        self.robot_moves = []
        self.goal = (self.gridWidth-1,self.gridHeight-1)
        print("Generating a grid..................................")

#The grid is created using inpuit from the user
    def createGrid(self):
        height = self.gridHeight
        width = self.gridWidth

        self.grid = [[random.randint(0,20) for i in range(0,height)] for j in range(0,width)]
        return self.grid

    def getGrid(self):
        return self.grid
        
    def get_robot_position(self):
        return (self.robot_x,self.robot_y)

    def move_left(self):
        if (self.robot_x > 0):
            self.robot_x -= 1  
            self.robot_moves.append((self.robot_x,self.robot_y))
            
    def move_right(self):
        if (self.robot_x < self.gridWidth-1):
            self.robot_x += 1  
            self.robot_moves.append((self.robot_x,self.robot_y))

    def move_up(self):
        if (self.robot_y > 0):
            self.robot_y -= 1  
            self.robot_moves.append((self.robot_x,self.robot_y))

    def move_down(self):
        if (self.robot_y < self.gridHeight-1):
            self.robot_y += 1  
            self.robot_moves.append((self.robot_x,self.robot_y))

    def my_algo(self):
        
        while self.get_robot_position()!=self.goal:
            current_cell = self.grid[self.robot_x][self.robot_y]
            
            right_cell = 1000000 if self.robot_x+1 > self.gridWidth-1 else self.grid[self.robot_x+1][self.robot_y] 
            down_cell = 1000000 if self.robot_y+1 > self.gridHeight-1 else self.grid[self.robot_x][self.robot_y+1] 
            print("robot at :",self.get_robot_position() ,"weight time is:", current_cell)
            if right_cell >= down_cell:
                self.move_down()
                
            else :
                self.move_right()

        print("Completed")
        print(self.robot_moves)
        self.show_robot_path()
        
    def show_robot_path(self):
        for move in self.robot_moves:
            self.grid[move[0]][move[1]] = "X"

            
#Visualisation of the grid
#Reference code from board.pypip ins
grid = creator()
grid.setup()
data = np.array(grid.createGrid())
print(data)
x = input("")
grid.my_algo()
board.checkerboard_table(np.array(grid.getGrid()), fmt='{:}')
pyplot.show()

