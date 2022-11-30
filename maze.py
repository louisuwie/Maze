# --------------------
# Function Definitions
# --------------------

array_maze = []
directions = ["North", "East", "South", "West"]

def print_maze(): # Assigned for printing the current maze 
    for x in array_maze:
        for y in x:
            print(y, end = " ")
        print()

def give_direction(): # Assigned for giving the possible directions
    directions = ["North", "East", "South", "West"]
    compass = ""
    
    for i in range(len(obstacles)):
        if obstacles[i] == 0:
            compass += directions[i] + " "
        else:
            continue

    print("Available Directions: " + compass)
    print("Which Path would you take?")

def create_maze_easy(): # Easy Maze, start [1][1], end [4][5]
    line_1 = ['■', '■', '■', '■', '■', '■']
    line_2 = ['■', '0', '■', '~', '~', '■']
    line_3 = ['■', '~', '~', '~', '■', '■']
    line_4 = ['■', '~', '■', '~', '~', '■']
    line_5 = ['■', '~', '■', '~', '■', '■']
    line_6 = ['■', '~', '■', '~', 'X', '■']
    line_7 = ['■', '■', '■', '■', '■', '■']

    array_maze.append(line_1)
    array_maze.append(line_2)
    array_maze.append(line_3)
    array_maze.append(line_4)
    array_maze.append(line_5)
    array_maze.append(line_6)
    array_maze.append(line_7)

    for x in array_maze:
        for y in x:
            print(y, end = " ")
        print()

def create_maze_normal(): # Normal Maze, start [1][1], end [6][7]
    line_1 = ['■', '■', '■', '■', '■', '■', '■', '■', '■']
    line_2 = ['■', '0', '~', '~', '~', '~', '~', '~', '■']
    line_3 = ['■', '~', '■', '■', '■', '■', '■', '~', '■']
    line_4 = ['■', '~', '~', '~', '~', '~', '■', '~', '■']
    line_5 = ['■', '~', '■', '■', '■', '~', '■', '■', '■']
    line_6 = ['■', '~', '■', '~', '■', '~', '~', '~', '■']
    line_7 = ['■', '~', '~', '~', '■', '~', '■', 'X', '■']
    line_8 = ['■', '■', '■', '■', '■', '■', '■', '■', '■']

    array_maze.append(line_1)
    array_maze.append(line_2)
    array_maze.append(line_3)
    array_maze.append(line_4)
    array_maze.append(line_5)
    array_maze.append(line_6)
    array_maze.append(line_7)
    array_maze.append(line_8)

    for x in array_maze:
        for y in x:
            print(y, end = " ")
        print()

def create_maze_hard(): # Hard Maze, start [1][1], end [7][8]
    line_1 = ['■', '■', '■', '■', '■', '■', '■', '■', '■','■']
    line_2 = ['■', '0', '~', '~', '~', '~', '~', '■', '~','■']
    line_3 = ['■', '~', '■', '■', '~', '■', '~', '~', '~','■']
    line_4 = ['■', '~', '~', '■', '~', '■', '~', '■', '■','■']
    line_5 = ['■', '■', '~', '■', '~', '■', '~', '~', '~','■']
    line_6 = ['■', '~', '~', '■', '~', '■', '■', '■', '~','■']
    line_7 = ['■', '~', '■', '~', '~', '■', '~', '■', '~','■']
    line_8 = ['■', '~', '■', '■', '■', '■', '~', '■', '~','■']
    line_9 = ['■', '~', '~', '~', '■', '■', '~', '~', 'X','■']
    line_10 =['■', '■', '■', '■', '■', '■', '■', '■', '■','■']

    array_maze.append(line_1)
    array_maze.append(line_2)
    array_maze.append(line_3)
    array_maze.append(line_4)
    array_maze.append(line_5)
    array_maze.append(line_6)
    array_maze.append(line_7)
    array_maze.append(line_8)
    array_maze.append(line_9)
    array_maze.append(line_10)

    for x in array_maze:
        for y in x:
            print(y, end = " ")
        print()

def find_player(): # Finds the x and y coordinates of the player within the current maze || Player symbol is 0
    y_num = 0
    x_num = 0

    coordinates = []
    for y in array_maze:
        for x in y:
            if x == '0':
                coordinates.append(x_num)
                coordinates.append(y_num)
                return coordinates
            x_num += 1
        x_num = 0
        y_num += 1

def check_obstacles(coord): # Checks what obstacles are around player
    cur_x = coord[0]
    cur_y = coord[1]
    
    # Check North, East, South, West -- respectively
    obstacles = [0,0,0,0]

    if array_maze[cur_y-1][cur_x] == '■': 
        obstacles[0] = 1
    if array_maze[cur_y][cur_x+1] == '■': 
        obstacles[1] = 1
    if array_maze[cur_y+1][cur_x] == '■': 
        obstacles[2] = 1
    if array_maze[cur_y][cur_x-1] == '■': 
        obstacles[3] = 1

    return obstacles

    ########################
    # PROGRAM RUN THE GAME #
    ########################
    
# Program Start, Choose Level
print("Welcome to the Maze!")
print("Select a level: 1, 2, or 3?")
userChoice = int(input())

#   ***WALLS ■***
#   ***PATH ◙***
#   ***PLAYER "0"***


#EASY LEVEL
if userChoice == 1:
    
    game = 1
    
    print('Easy Level!')
    create_maze_easy()
    coord = find_player()
    obstacles = check_obstacles(coord)
    
    while game > 0:
        
        give_direction()
        userMove = input()
        
        if userMove.lower() == "north" and obstacles[0] == 0:
            
            array_maze[coord[1]][coord[0]] = "◙" #Changes the current position into ***PATH***
            array_maze[coord[1]-1][coord[0]] = "0" #Changes the next position into ***PLAYER***
            coord = find_player()
            obstacles = check_obstacles(coord)
            
            if array_maze[coord[1]][coord[0]] == array_maze[5][4]: #Checks if the player has reached the Exit.
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
            print_maze()
        elif userMove.lower() == "east" and obstacles[1] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙"
            array_maze[coord[1]][coord[0]+1] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[5][4]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "south" and obstacles[2] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙"
            array_maze[coord[1]+1][coord[0]] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[5][4]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "west" and obstacles[3] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙" 
            array_maze[coord[1]][coord[0]-1] = "0" 
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[5][4]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
                
            
        elif userMove.lower() == "quit":
            print("Try again next time. \nGoodbye.")
            game = 0
        
        else:
            print("Please choose an available direction!")
            
#NORMAL LEVEL
if userChoice == 2:
    
    game = 1
    
    print('Normal Level!')
    create_maze_normal()
    coord = find_player()
    obstacles = check_obstacles(coord)
    
    while game > 0:
         
        give_direction()
        userMove = input()
        
        if userMove.lower() == "north" and obstacles[0] == 0:
            array_maze[coord[1]][coord[0]] = "◙"#Changes current position to "Path symbol"
             
            array_maze[coord[1]-1][coord[0]] = "0"#Changes new position to player symbol
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[6][7]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "east" and obstacles[1] == 0:
            array_maze[coord[1]][coord[0]] = "◙"
             
            array_maze[coord[1]][coord[0]+1] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()

            if array_maze[coord[1]][coord[0]] == array_maze[6][7]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "south" and obstacles[2] == 0:
            array_maze[coord[1]][coord[0]] = "◙"
             
            array_maze[coord[1]+1][coord[0]] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[6][7]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "west" and obstacles[3] == 0:
            array_maze[coord[1]][coord[0]] = "◙"
             
            array_maze[coord[1]][coord[0]-1] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()

            if array_maze[coord[1]][coord[0]] == array_maze[6][7]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "quit":
            print("Try again next time \nGoodbye")
            game = 0
        
        else:
            print("Please choose a valid direction!")
            
                
                
#HARD LEVEL
if userChoice == 3:
    
    game = 1
    
    print('Hard Level!')
    create_maze_hard()
    coord = find_player()
    obstacles = check_obstacles(coord)
    
    while game > 0:
        
        give_direction()
        userMove = input()
        
        if userMove.lower() == "north" and obstacles[0] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙"
            array_maze[coord[1]-1][coord[0]] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[8][8]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "east" and obstacles[1] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙"
            array_maze[coord[1]][coord[0]+1] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()

            if array_maze[coord[1]][coord[0]] == array_maze[8][8]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "south" and obstacles[2] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙"
            array_maze[coord[1]+1][coord[0]] = "0"
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[8][8]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "west" and obstacles[3] == 0:
             
            array_maze[coord[1]][coord[0]] = "◙" #Changes current position to "Path symbol"
            array_maze[coord[1]][coord[0]-1] = "0" #Changes new position to player symbol
            coord = find_player()
            obstacles = check_obstacles(coord)
            print_maze()
            
            if array_maze[coord[1]][coord[0]] == array_maze[8][8]:
                print("Found the Exit!\nGoodbye!")
                game += 1
                break
            
        elif userMove.lower() == "quit":
            print("Try again next time \nGoodbye")
            game = 0
        
        else:
            print("Please choose a valid direction!")

#FINISHED