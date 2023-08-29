class Spacecraft:

    # list of direction
    DIRECTION = ['n','e','s','w']

    # for finding the final index
    direction_index = 0

    # default condition of the spacecraft
    POSITION = (0,0,0)

    # actual direction of the spacecraft
    REAL_DIRECTION = ''

    # initialize the variable with the given data using constructor
    def __init__(self,position,direction):

        self.REAL_DIRECTION = direction
        self.POSITION = position

        # if initial condition is 'up' or 'down' we set the default direction north
        if direction in ['u','d']:
            self.direction_index = 0
        else:
            self.direction_index = self.DIRECTION.index(direction)

    # function that handle the backword/forward Condition
    def Move(self,distance):
        self.POSITION = (self.POSITION[0]+distance[0],self.POSITION[1]+distance[1],self.POSITION[2]+distance[2])
    
    # function that handle the up and down condition of the spacecraft
    def move_up_down(self,direction):
        self.REAL_DIRECTION = direction

    # function that handle the change in the direction for 'LEFT' and 'Right'condition
    def Turn(self,direction):

        if direction == 'l':
            if self.direction_index == 0:
                self.direction_index = 3
            else:
                self.direction_index -= 1
            self.REAL_DIRECTION = self.DIRECTION[self.direction_index]
        else:
            if self.direction_index == 3:
                self.direction_index == 0
            else:
                self.direction_index += 1
                self.REAL_DIRECTION = self.DIRECTION[self.direction_index]

    # function that handle the navigation according to the given command
    def navigate(self,command):

        for comm in command:
            if comm in ['l','r']:
                self.Turn(comm)
            if comm in ['u','d']:
                self.move_up_down(comm)
            if comm in ['f','b']:
                value = 1 if comm=='f' else -1

                if self.REAL_DIRECTION in ['e','w']:
                    x,y,z = value,0,0
                elif self.REAL_DIRECTION in ['n','s']:
                    x,y,z = 0,value,0
                else:
                    x,y,z = 0,0,value
                distance = (x,y,z)
                self.Move(distance)
        # it simply return the new direction and new position after executing the all command
        return self.POSITION,self.REAL_DIRECTION
    
