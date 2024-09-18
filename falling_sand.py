from os import system, name
from time import sleep
import random as rnd
from pynput import keyboard

grid = []
cols = 100
rows = 30

sand = "■"
empty = " "

# Create grid filled with empty cells
for _ in range(rows):
    row = []
    for _ in range(cols):
        row.append(empty)
    grid.append(row)
    
def add_sand():
    grid[0][sand_x] = sand
    
sand_x = cols // 2

def on_press(key):
    global sand_x

    if key == keyboard.Key.right:
        sand_x = min(sand_x + 1, cols - 1)
    if key == keyboard.Key.left:
        sand_x = max(sand_x - 1, 0)


def print_grid():
    for row in grid:
        print(*row)

def clear_console():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For macOS and Linux
    else:
        _ = system('clear')
        


# Set up the keyboard listener
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Main loop
while True:    
    clear_console()
    add_sand()
    
    # Update sand positions
    for i in range(len(grid)-1,-1,-1): # iterate from bottom to top
        for j in range(len(grid[i])):

            if grid[i][j] == sand:
                if i+1 < rows and j+1 < cols and j-1 > 0:
                    grid[i][j] = empty
                    
                    dir = rnd.choice([-1, 0, 1])
                    if grid [i+1][j] == empty: # below
                        grid[i+1][j] = sand
                    elif grid [i+1][j+dir] == empty: # right/left
                        grid[i+1][j+dir] = sand
                    else:
                        grid[i][j] = sand
                        
    print_grid()
    sleep(0.1)