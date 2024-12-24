def get_input(filename):
    input = []
    with open(filename) as file:
        for line in file.readlines():
            input.append([c for c in line.strip()])
    return input


def get_unique_antinode_locations(grid):
    length = len(grid)
    height = len(grid[0])
    antennas = {}
    for r in range(length):
        for c in range(height):
            char = grid[r][c]
            if char != '.':
                if char not in antennas:
                    antennas[char] = [(r, c)]
                else:
                    antennas[char].append((r, c))

    antenna_pairs = []
    for antenna in antennas:
        for i in range(len(antennas[antenna])):
            for j in range(i + 1, len(antennas[antenna])):
                antenna_pairs.append((antennas[antenna][i], antennas[antenna][j]));

    antinodes = set()
    
    for antenna_pair in antenna_pairs:
        antenna_0 = antenna_pair[0]
        antenna_1 = antenna_pair[1]
        dx = antenna_1[0] - antenna_0[0]
        dy = antenna_1[1] - antenna_0[1]

        antinode_x = antenna_0[0] - dx
        antinode_y = antenna_0[1] - dy
        
        if (antinode_x >= 0 and antinode_y >= 0
        and antinode_x < length and antinode_y < height):
            antinodes.add((antinode_x, antinode_y))

        antinode_x = antenna_1[0] + dx
        antinode_y = antenna_1[1] + dy
        
        if (antinode_x >= 0 and antinode_y >= 0
        and antinode_x < length and antinode_y < height):
            antinodes.add((antinode_x, antinode_y))

    return antinodes


def get_all_unique_antinode_locations(grid):
    length = len(grid)
    height = len(grid[0])
    antennas = {}
    for r in range(length):
        for c in range(height):
            char = grid[r][c]
            if char != '.':
                if char not in antennas:
                    antennas[char] = [(r, c)]
                else:
                    antennas[char].append((r, c))

    antenna_pairs = []
    for antenna in antennas:
        for i in range(len(antennas[antenna])):
            for j in range(i + 1, len(antennas[antenna])):
                antenna_pairs.append((antennas[antenna][i], antennas[antenna][j]));

    antinodes = set()
    
    for antenna_pair in antenna_pairs:
        antenna_0 = antenna_pair[0]
        antenna_1 = antenna_pair[1]
        
        antinodes.add((antenna_0[0], antenna_0[1]))
        antinodes.add((antenna_1[0], antenna_1[1]))

        dx = antenna_1[0] - antenna_0[0]
        dy = antenna_1[1] - antenna_0[1]

        antinode_x = antenna_0[0] - dx
        antinode_y = antenna_0[1] - dy

        while (antinode_x >= 0 and antinode_y >= 0
                and antinode_x < length and antinode_y < height):
            antinodes.add((antinode_x, antinode_y))
            antinode_x = antinode_x - dx
            antinode_y = antinode_y - dy
        
        antinode_x = antenna_1[0] + dx
        antinode_y = antenna_1[1] + dy
        
        while (antinode_x >= 0 and antinode_y >= 0
                and antinode_x < length and antinode_y < height):
            antinodes.add((antinode_x, antinode_y))
            antinode_x = antinode_x + dx
            antinode_y = antinode_y + dy
        
    return antinodes


filename = 'inputs/day8.txt'
input = get_input(filename)

print(f'unique antinode locations = {len(get_unique_antinode_locations(input))}')
print(f'all unique antinode locations = {len(get_all_unique_antinode_locations(input))}')
