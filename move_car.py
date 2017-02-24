"""
There should be some descriptions of the code.

ex:

input:
8 8
1 4 E
RMLLM
4 5 N
LMRML

output:
1 4 N
3 6 W
"""
class Vehicle():
    directions = 'NESW' 
    movement = {'N': (0,1), 'E': (1,0), 'S': (0,-1), 'W':(-1,0)}

    def __init__(self, x, y, face, grid, obstacle):
        self.x = x
        self.y = y
        self.dir = face
	self.grid_width, self.grid_height = grid
        self.obstacle = obstacle

    def turn_left(self):
        self.dir = self.directions[(self.directions.index(self.dir)-1)%len(self.directions)]

    def turn_right(self):
        self.dir = self.directions[(self.directions.index(self.dir)+1)%len(self.directions)]
  
    def Uturn(self):
        self.dir = self.directions[(self.directions.index(self.dir)+2)%len(self.directions)]

    def excute_command(self, commands):
        action = {
		'L': self.turn_left,
		'R': self.turn_right,
		'M': self.move,
		}
	for command in commands:
	    action[command]()

    def move(self):
        new_x = self.x + self.movement[self.dir][0]
        new_y = self.y + self.movement[self.dir][1]

        if (new_x, new_y) != self.obstacle and 0<=new_x<=self.grid_width and 0<=new_y<=self.grid_height:
	    self.x = new_x
	    self.y = new_y 

    def direction(self):
        return self.dir

    def position(self):
        return (self.x, self.y)

def move_vehicle(grid, obstacle):
    vehicle_pos  = raw_input().split()
    vehicle = Vehicle(int(vehicle_pos[0]), int(vehicle_pos[1]), vehicle_pos[2], grid, obstacle)
    vehicle.excute_command(raw_input().strip())
    return vehicle.position, vehicle.direction

def main():
    grid = map(int, raw_input().split())
    vehicle_one_pos, vehicle_one_dir = move_vehicle(grid, None)
    vehicle_two_pos, vehicle_two_dir = move_vehicle(grid, vehicle_one_pos)
    print vehicle_one_pos[0], vehicle_one_pos[1], vehicle_one_dir
    print vehicle_two_pos[0], vehicle_two_pos[1], vehicle_two_dir

if __name__ == '__main__':
    main()
