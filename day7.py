def get_input(filename):
    targets = []
    inputs = []
    with open(filename) as file:
        for line in file.readlines():
            target, input = line.split(':')
            targets.append(int(target.strip()))
            inputs.append([int(x) for x in input.strip().split()])
    return targets, inputs


def equation_possible(target, input, curr, i):
    if curr > target or i > len(input):
        return False

    if i == len(input):
        if curr != target:
            return False
        else:
            return True

    return (equation_possible(target, input, curr + input[i], i + 1)
        or equation_possible(target, input, curr * input[i], i + 1))
    

def equation_possible_with_concatenation(target, input, curr, i):
    if curr > target or i > len(input):
        return False

    if i == len(input):
        if curr != target:
            return False
        else:
            return True

    concat = int(str(curr) + str(input[i]))
    return (equation_possible_with_concatenation(target, input, curr + input[i], i + 1)
    or equation_possible_with_concatenation(target, input, curr * input[i], i + 1)
    or equation_possible_with_concatenation(target, input, concat, i + 1))


def calculate_calibration_result(targets, inputs):
    sum = 0
    for i in range(len(targets)):
        if equation_possible(targets[i], inputs[i], 0, 0):
            sum += targets[i]
    return sum
        

def calculate_new_calibration_result(targets, inputs):
    sum = 0
    for i in range(len(targets)):
        if equation_possible_with_concatenation(targets[i], inputs[i], 0, 0):
            sum += targets[i]
    return sum


filename = 'inputs/day7.txt'
targets, inputs = get_input(filename)

print(f'total calibration result = {calculate_calibration_result(targets, inputs)}')

print(f'new total calibration result = {calculate_new_calibration_result(targets, inputs)}')

