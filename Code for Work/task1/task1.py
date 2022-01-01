#imports
from matplotlib import pyplot
import numpy as np
import random
import board
from queue import PriorityQueue

algo1stats = 0;
algo2stats = 0;

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
        
#Return the bot back to the start position        
    def reset_robot_position(self):
        self.robot_x = 0
        self.robot_y = 0
        return True

#Returns the bot's current position
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

#Heuristic algo, can only move down and right, will determine which is smaller and move to that block
    def my_algo(self):

        algo1totalWaitTime = 0
        self.reset_robot_position()
        
        while self.get_robot_position()!=self.goal:
            current_cell = self.grid[self.robot_x][self.robot_y]
            algo1totalWaitTime += current_cell

            right_cell = 1000000 if self.robot_x+1 > self.gridWidth-1 else self.grid[self.robot_x+1][self.robot_y] 
            down_cell = 1000000 if self.robot_y+1 > self.gridHeight-1 else self.grid[self.robot_x][self.robot_y+1] 
            print("robot at :",self.get_robot_position() ,"weight time is:", current_cell)
            if right_cell >= down_cell:
                self.move_down()
                
            else :
                self.move_right()

        print("Completed\nThe total wait time was", + algo1totalWaitTime)
        print(self.robot_moves)

    def my_algo2(self):

        algo2totalWaitTime = 0
        movingCellValue = 0
        self.reset_robot_position()
        
        while self.get_robot_position()!=self.goal:
            current_cell = self.grid[self.robot_x][self.robot_y]
            algo2totalWaitTime += abs(current_cell-movingCellValue)

            right_cell = 1000000 if self.robot_x+1 > self.gridWidth-1 else self.grid[self.robot_x+1][self.robot_y] 
            down_cell = 1000000 if self.robot_y+1 > self.gridHeight-1 else self.grid[self.robot_x][self.robot_y+1] 
            print("robot at :",self.get_robot_position() ,"weight time is:", current_cell)
            if abs(right_cell - current_cell) >= abs(down_cell-current_cell):
                self.movingCellValue=current_cell
                self.move_down()
                
            else :
                self.movingCellValue=current_cell
                self.move_right()

        print("Completed\nThe total wait time was", + algo2totalWaitTime)
        print(self.robot_moves)
        self.show_robot_path()
        
    def show_robot_path(self):
        for move in self.robot_moves:
            self.grid[move[0]][move[1]].set_bad(color='red')

    # def dijktra_algo(self):

#Visualisation of the grid
#Reference code from board.pypip ins
grid = creator()
grid.setup()
data = np.array(grid.createGrid())
print(data)

while True:
    choice = input("Select Game Mode One or Two:\nEnter 1 for time spent on cell equal to its cell value\nEnter 2 for time on cell equal to absolute difference between current and previous\nEnter 3 Change Grid Specification\nEnter 4 to see performace infromation\n")
    
    if choice in ('1', '2','3','4'):

        if choice == "1":
            print("Performing heuristic algorithm:") 
            print("............................")
            grid.my_algo()
            board.checkerboard_table(np.array(grid.getGrid()), fmt='{:}')
            pyplot.show()
            print("Performing dijkstra's algorithm:") 
            print("............................")

        elif choice == "2":
            print("Performing heuristic algorithm:") 
            print("............................")
            grid.my_algo2()
            board.checkerboard_table(np.array(grid.getGrid()), fmt='{:}')
            pyplot.show()
            print("Performing dijkstra's algorithm:") 
            print("............................")

        elif choice == "3":
            grid = creator()
            grid.setup()
            data = np.array(grid.createGrid())
            print(data)

        elif choice == "4":
            grid = creator()
            grid.setup()
            data = np.array(grid.createGrid())
            print(data)

        nextStep = input("Try another function? (yes/no)\n")
        if nextStep == "no":
          break

    else:
        print("Invalid output")          