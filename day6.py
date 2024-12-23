def get_input(filename):
    input = []
    with open(filename) as file:
        for line in file.readlines():
            curr = []
            for c in line.strip():
                curr.append(c)
            input.append(curr)
    return input


def get_guard_starting_position(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '^':
                return (r, c)


def map_guard_path(grid):
    visited = set()

    guard_movement = {
        'UP': (-1, 0),
        'RIGHT': (0, 1),
        'DOWN': (1, 0),
        'LEFT': (0, -1),
    }

    gx, gy = get_guard_starting_position(grid)   
    guard_facing = 'UP'

    while True:
        new_gx = gx + guard_movement[guard_facing][0]
        new_gy = gy + guard_movement[guard_facing][1]

        if (new_gx < 0 or new_gy < 0
        or new_gx >= len(grid) or new_gy >= len(grid[0])):
            visited.add((gx, gy))
            return visited

        if grid[new_gx][new_gy] == '#':
            if guard_facing == 'UP':
                guard_facing = 'RIGHT'
            elif guard_facing == 'RIGHT':
                guard_facing = 'DOWN'
            elif guard_facing == 'DOWN':
                guard_facing = 'LEFT'
            elif guard_facing == 'LEFT':
                guard_facing = 'UP'
        else: 
            visited.add((gx, gy))      
            gx, gy = new_gx, new_gy


def guard_loops(grid):
    guard_movement = {
        'UP': (-1, 0),
        'RIGHT': (0, 1),
        'DOWN': (1, 0),
        'LEFT': (0, -1),
    }

    gx, gy = get_guard_starting_position(grid)   
    guard_facing = 'UP'

    guard_positions = set()

    while True:
        new_gx = gx + guard_movement[guard_facing][0]
        new_gy = gy + guard_movement[guard_facing][1]

        if (new_gx < 0 or new_gy < 0
        or new_gx >= len(grid) or new_gy >= len(grid[0])):
            return False

        if grid[new_gx][new_gy] == '#':
            if guard_facing == 'UP':
                guard_facing = 'RIGHT'
            elif guard_facing == 'RIGHT':
                guard_facing = 'DOWN'
            elif guard_facing == 'DOWN':
                guard_facing = 'LEFT'
            elif guard_facing == 'LEFT':
                guard_facing = 'UP'
        else: 
            guard_position = ((guard_facing, gx, gy))
            if guard_position in guard_positions:
                return True
            guard_positions.add(guard_position)
            gx, gy = new_gx, new_gy


def count_obstacle_positions(grid):
    # only need to check positions guard reached before new obstacle
    # -> other positions on the grid are unreachable

    count = 0
    positions = map_guard_path(input) 
    for position in positions:
        r, c = position[0], position[1]
        if grid[r][c] != '#' and grid[r][c] != '^':
            old_char = grid[r][c]
            grid[r][c] = '#'
            if guard_loops(grid):
                count += 1
            grid[r][c] = old_char
        
    return count

filename = 'inputs/day6.txt'
input = get_input(filename)

print(f'unique guard positions = {len(map_guard_path(input))}')

print(f'positions for new obstacle = {count_obstacle_positions(input)}')
