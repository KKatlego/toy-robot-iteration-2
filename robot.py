
def get_robot_name():
    """Gets robot's name from the user."""
    name = input("What do you want to name your robot? ")
    return name


def print_greeting(name):
    """Displays the greeting along with the robot name."""
    print(f'{name}: Hello kiddo!')


def get_input_command(name):
    """Asks the user to input a command for the robot to do."""
    command = input(f"{name}: What must I do next? ")
    return command


def forward_command(command):
    """This function creates a list with the first index being 
    the forward command and the second index being an integer."""
    forward = command.split()
    steps = int(forward[1])
    return command, forward, steps


def print_moved_forward(name, steps):
    """Displays the number of steps moved forward by the robot."""
    print(f" > {name} moved forward by {steps} steps.")


def sprint_command(command):
    """This function creates a list with the first index being 
    the sprint command and the second index being an integer."""
    sprint = command.split()
    steps = int(sprint[1])
    return command, sprint, steps


def back_command(command):
    """This function creates a list with the first index being 
    the back command and the second index being an integer."""
    back = command.split()
    steps = int(back[1])
    return command, back, steps


def print_moved_back(name, steps):
    """Displays the number of steps moved back by the robot."""
    print(f" > {name} moved back by {steps} steps.")


def right_output(name):
    """This function prints that the robot turned right."""
    print(f" > {name} turned right.")


def left_output(name):
    """This function prints that the robot turned left."""
    print(f" > {name} turned left.")


def left_command(command, degrees):
    """Controls the direction of the robot turning left considering 
    the position it is currently at in degrees."""
    if command == 'left' and degrees == 0:
        degrees = 270
    elif command == 'left' and degrees == 90:
        degrees = 0
    elif command == 'left' and degrees == 180:
        degrees = 90
    elif command == 'left' and degrees == 270:
        degrees = 180
    return degrees


def track_position(name, steps, x, y, command, degrees):
    """"This function tracks the position of the robot as it moves:
    -Takes in the forward movement: Robot moves forward .
    -Takes in the back movement: Robot moves back.
    -Takes in the sprint movement: Robot sprints forward.
    """
    new_y = y
    new_x = x
    if command == 'forward':
        if degrees == 0:
            if y + steps > 200:
                robot_area(name,x,y)
            else:  
                new_y = y + steps
                print_moved_forward(name, steps)
        elif degrees == 180:
            if y - steps < -200:
                robot_area(name,x,y)
            else:
                new_y = y - steps
                print_moved_forward(name, steps)
        elif degrees == 90:
            if x + steps > 100:
                robot_area(name,x,y)
            else:
                new_x = x + steps
                print_moved_forward(name, steps)
        elif degrees == 270:
            if x - steps < -100:
                robot_area(name,x,y)
            else:
                new_x = x - steps
                print_moved_forward(name, steps)
        
    if command == 'back':
        if degrees == 0:
            if y - steps < -200:
                robot_area(name,x,y)
            else:
                new_y = y - steps
                print(f" > {name} moved back by {steps} steps.")
        elif degrees == 180:
            if y + steps > 200:
                robot_area(name,x,y)
            else:
                new_y = y + steps
                print(f" > {name} moved back by {steps} steps.")
        elif degrees == 90:
            if x - steps < -100:
                robot_area(name,x,y)
            else:
                new_x = x - steps
                print(f" > {name} moved back by {steps} steps.")
        elif degrees == 270:
            if x + steps > 100:
                robot_area(name,x,y)
            else:
               new_x = x + steps
               print(f" > {name} moved back by {steps} steps.")

    if command == 'sprint':
        if steps == 0:
            return x, y
        else:
            if degrees == 0:
                if y + steps > 200:
                    robot_area(name,x,y)
                else:  
                    new_y = y + steps
                    print_moved_forward(name, steps)
            elif degrees == 180:
                if y - steps < -200:
                    robot_area(name,x,y)
                else:
                    new_y = y - steps
                    print_moved_forward(name, steps)
            elif degrees == 90:
                if x + steps > 100:
                    robot_area(name,x,y)
                else:
                    new_x = x + steps
                    print_moved_forward(name, steps)
            elif degrees == 270:
                if x - steps < -100:
                    robot_area(name,x,y)
                else:
                    new_x = x - steps
                    print_moved_forward(name, steps)

    if command == 'right':
       new_y = y
    if command == 'sprint':
        if steps == 1:
            print(f" > {name} now at position ({new_x},{new_y}).")
            return track_position(name, steps - 1, new_x, new_y, command, degrees)
        else:
            return track_position(name, steps - 1, new_x, new_y, command, degrees)
    else:
        print(f" > {name} now at position ({new_x},{new_y}).")
    return new_x, new_y


def off_command(command, name):
    """This function takes in the off command that switches the robot off."""
    if command.lower() == "off":
        print(f"{name}: Shutting down..")
    return command


def robot_area(name,x,y):
    """This function tells the user it cannot exceed its area:
    -x outside the range(-100,100)
    -y outside the range(-200,200)"""
    print(f"{name}: Sorry, I cannot go outside my safe zone.")
    return x, y


def help_command():
    """The help command tells the child what the possible commands are."""
    understand = "I can understand these commands:"
    off = "OFF  - Shut down robot"
    help_me = "HELP - provide information about commands"
    forward = "FORWARD  - Moves robot forward"
    back = "BACK  - Moves robot backward"
    right = "RIGHT  - Turns robot 90 degrees to the right"
    left = "LEFT  - Turns robot 90 degrees to the left"
    return f"{understand}\n{off}\n{help_me}\n{forward}\n{back}\n{right}\n{left}"


def check_valid_commands(command, name):
    """This function takes in only a list of valid commands that the user can enter.

    If a command is not in the list 
    the robot tells the user that it does not understand the unknown command.
    """
    valid_commands = ['off', 'help', 'forward', 'back', 'right', 'left', 'sprint']
    for i in valid_commands:
        if i in command.lower():
            return True
    print(f"{name}: Sorry, I did not understand '{command}'.")
    return False
    

def robot_start():
    """This is the main function of the program calling most functions
    and controlling all the movements of the robot, 
    while the user entered a valid command"""
    name = get_robot_name()
    print_greeting(name)
    x = 0
    y = 0
    degrees = 0
    while True:
        command = get_input_command(name)
        if check_valid_commands(command, name) is True:
            command = command.lower()
            if 'help' in command:
                print(help_command())
            elif 'forward' in command:
                if command == "forward" or command[8:].isdigit() == False:
                     print(f"{name}: Sorry, I did not understand '{command}'.")
                else:
                    command, forward, steps = forward_command(command)
                    x, y = track_position(name, steps, x, y, forward[0],degrees)
            elif 'back' in command:
                if command == "back" or command[5:].isdigit() == False:
                    print(f"{name}: Sorry, I did not understand '{command}'.")
                else:
                    command, back, steps = back_command(command)
                    x, y = track_position(name, steps, x, y, back[0], degrees)
            elif 'right' in command:
                right_output(name)
                degrees += 90
                x, y = track_position(name, 0, x, y, command,0)
            elif 'left' in command:
                degrees = left_command(command, degrees)
                left_output(name)
                x, y = track_position(name, 0, x, y, command,degrees)
            elif 'sprint' in command:
                if command == "sprint" or command[7:].isdigit() == False:
                     print(f"{name}: Sorry, I did not understand '{command}'.")
                else:
                    command, sprint, steps = sprint_command(command)
                    x, y = track_position(name, steps, x, y, sprint[0],degrees)
            elif 'off' in command:
                off_command(command, name)
                break
                

if __name__ == "__main__":
    robot_start()

