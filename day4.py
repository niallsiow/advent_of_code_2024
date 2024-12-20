def is_valid_position(grid, r, c, position):
    for char in position:
        dr = position[char][0]
        dc = position[char][1]
        n_r = r + dr
        n_c = c + dc
        if (n_r < 0 or n_c < 0
        or n_r >= len(grid) or n_c >= len(grid[0])
        or grid[n_r][n_c] != char):
            return False
    return True


def get_xmas_counts_at_index(grid, r, c):
    counts = 0

    positions = [
        {'M': [0, 1], 'A': [0, 2], 'S': [0, 3]},       # left->right
        {'M': [0, -1], 'A': [0, -2], 'S': [0, -3]},    # right->left
        {'M': [1, 0], 'A': [2, 0], 'S': [3, 0]},       # top->bottom
        {'M': [-1, 0], 'A': [-2, 0], 'S': [-3, 0]},    # bottom->top
        {'M': [1, 1], 'A': [2, 2], 'S': [3, 3]},       # topleft->bottomright
        {'M': [-1, -1], 'A': [-2, -2], 'S': [-3, -3]}, # bottomright->topleft
        {'M': [1, -1], 'A': [2, -2], 'S': [3, -3]},    # topright->bottomleft
        {'M': [-1, 1], 'A': [-2, 2], 'S': [-3, 3]},    # bottomleft->topright
    ]

    for position in positions:
        if is_valid_position(grid, r, c, position):
            counts += 1

    return counts


def xmas_counts(grid):
    counts = 0
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'X':
               counts += get_xmas_counts_at_index(grid, r, c)
 
    return counts


def cross_mas_present(grid, r, c):
    left_down_positions = [
        {'M': [-1, -1], 'S': [1, 1]},
        {'S': [-1, -1], 'M': [1, 1]}
    ]

    right_down_positions = [
        {'M': [1, -1], 'S': [-1, 1]},
        {'S': [1, -1], 'M': [-1, 1]}
    ]

    for position in left_down_positions:
        if is_valid_position(grid, r, c, position):
            for position in right_down_positions:
                if is_valid_position(grid, r, c, position):
                    return True

    return False


def cross_mas_counts(grid):
    counts = 0

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'A':
                if cross_mas_present(grid, r, c):
                    counts += 1

    return counts           


def get_input(filename):
    input = []

    with open(input_file) as file:
        lines = file.readlines()
    
        for line in lines:
            curr = []
            for c in line.strip():
                curr.append(c)
            input.append(curr)
    return input


input_file = 'inputs/day4.txt'
input = get_input(input_file)

print(f'xmas appears {xmas_counts(input)} times')
print(f'x-mas appears {cross_mas_counts(input)} times')
