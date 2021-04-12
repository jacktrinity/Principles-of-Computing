"""
Week 2 Mini-Project of Principles of Computing
CodeSkulptor: http://www.codeskulptor.org/#user48_lrXfjBE5BNCwOY6.py

Written in Python 2
"""

# Clone of 2048 game.

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def add_missing_zero(a_list):
        """
        Add appropriate number of zeroes at the end of the list.
        """
        while len(a_list) < len(line):
            a_list.append(0)
        return a_list
    
    def non_zero_slide(b_list):
        """
        Iterate over the input and create an output list that has all 
        of the non-zero tiles slid over to the beginning of the list.
        """
        append_list = []
        for dummy_num in b_list:
            if dummy_num > 0:
                append_list.append(dummy_num)
        return append_list
        
    lst1 = non_zero_slide(line)
    lst1 = add_missing_zero(lst1)
    
    # merging numbers
    num = 0
    while num < len(lst1) - 1:
        if lst1[num] == lst1[num + 1]:
            lst1[num] = lst1[num] * 2
            lst1[num + 1] = 0
        num += 1
        
    lst2 = non_zero_slide(lst1)
    lst2 = add_missing_zero(lst2)
        
    return lst2


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._height = grid_height
        self._width = grid_width
        self._grid = []
        
        for dummy_i in range(self._height):
            row = []
            for dummy_j in range(self._width):
                row.append(0)
                
            self._grid.append(row)
        
    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid 
        in a linear direction.
    
        Both start_cell is a tuple(row, col) denoting the 
        starting cell.
    
        Direction is a tuple that difference between
        consecutive cells in the traversal.
        """
        
        # Travering and getting the value from the grid (row, col)
        traverse_list = []
        for steps in range(num_steps):
            row = start_cell[0] + steps * direction[0]
            col = start_cell[1] + steps * direction[1]
                
            value = self.get_tile(row, col)
            traverse_list.append(value)
        
        return traverse_list
    
    def merge_grid(self, start_cell, direction, num_steps, traverse_lst):
        """
        Apply merge function and then set tiles with the new merge list.
        """
        
        merge_list = merge(traverse_lst)
        
        for steps in range(num_steps):
            row = start_cell[0] + steps * direction[0]
            col = start_cell[1] + steps * direction[1]
            self.set_tile(row, col, merge_list[steps])
        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = []
        
        for dummy_i in range(self._height):
            row = []
            for dummy_j in range(self._width):
                row.append(0)
                
            self._grid.append(row)
        
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return_string = ""
        for row in self._grid:
            return_string += str(row) + "\n"
            
        return return_string

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        old_grid = []
        new_grid = []
        
        if direction == LEFT:
            for left_num in range(self._height):
                old_lst = self.traverse_grid((left_num, 0), OFFSETS[direction], self._width)
                self.merge_grid((left_num, 0), OFFSETS[direction], self._width, old_lst)
                
                new_lst = merge(old_lst)
                old_grid.append(old_lst)
                new_grid.append(new_lst)
                
            if old_grid != new_grid:
                self.new_tile()
                
        elif direction == RIGHT:
            for right_num in range(self._height):
                old_lst = self.traverse_grid((right_num, self._width - 1), OFFSETS[direction], self._width)
                self.merge_grid((right_num, self._width - 1), OFFSETS[direction], self._width, old_lst)
                
                new_lst = merge(old_lst)
                old_grid.append(old_lst)
                new_grid.append(new_lst)
                
            if old_grid != new_grid:
                self.new_tile()
                
        elif direction == UP:
            for up_num in range(self._width):
                old_lst = self.traverse_grid((0, up_num), OFFSETS[direction], self._height)
                self.merge_grid((0, up_num), OFFSETS[direction], self._height, old_lst)
                
                new_lst = merge(old_lst)
                old_grid.append(old_lst)
                new_grid.append(new_lst)
                
            if old_grid != new_grid:
                self.new_tile()
                
        elif direction == DOWN:
            for down_num in range(self._width):
                old_lst = self.traverse_grid((self._height - 1, down_num), OFFSETS[direction], self._height)
                self.merge_grid((self._height - 1, down_num), OFFSETS[direction], self._height, old_lst)
                
                new_lst = merge(old_lst)
                old_grid.append(old_lst)
                new_grid.append(new_lst)
                
            if old_grid != new_grid:
                self.new_tile()
 
           
    def check_empty_tile(self):
        """
        Check if there is any empty tile left inside the grid
        """
        for each_grid in self._grid:
            if 0 in each_grid:
                return True
        return False
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        if self.check_empty_tile(): 
            random_row = random.randrange(0, self._height)
            random_col = random.randrange(0, self._width)
        
            if self.get_tile(random_row, random_col) == 0:
                random_num = random.randint(1, 10)
                if random_num == 1:
                    self.set_tile(random_row, random_col, 4)
                else:
                    self.set_tile(random_row, random_col, 2)
            else:
                return self.new_tile()
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
