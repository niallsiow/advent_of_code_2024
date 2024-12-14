from enum import Enum


class ParserState(Enum):
    SEARCHING = 1
    VALIDATE_MUL = 2
    PARSE_VAL1 = 3
    PARSE_VAL2 = 4
    CHECK_ENABLE = 5


def sum_uncorrupted_muls(input):
    state = ParserState.SEARCHING

    curr = ''
    val1 = 0
    val2 = 0

    sum = 0

    for i in range(len(input)):
        if input[i] == 'm':
            curr = ''
            state = ParserState.VALIDATE_MUL

        if state == ParserState.VALIDATE_MUL:
            curr += input[i]
            if curr == 'mul(':
                curr = ''
                state = ParserState.PARSE_VAL1
        elif state == ParserState.PARSE_VAL1:
            if input[i] == ',':
                val1 = int(curr)
                curr = ''
                state = ParserState.PARSE_VAL2
                continue

            curr += input[i]
            if not input[i].isdigit():
                state = ParserState.SEARCHING
            elif len(curr) > 3:
                state = ParserState.SEARCHING
        elif state == ParserState.PARSE_VAL2:
            if input[i] == ')':
                val2 = int(curr)
                sum += val1 * val2
                state = ParserState.SEARCHING
                continue
             
            curr += input[i]
            if not input[i].isdigit():
                state = ParserState.SEARCHING
            elif len(curr) > 3:
                state = ParserState.SEARCHING

    return sum


def sum_enabled_uncorrupted_muls(input):
    state = ParserState.SEARCHING

    enable = True

    curr = ''
    val1 = 0
    val2 = 0

    sum = 0

    for i in range(len(input)):
        if input[i] == 'm':
            curr = ''
            state = ParserState.VALIDATE_MUL
        if input[i] == 'd':
            curr = ''
            state = ParserState.CHECK_ENABLE


        if state == ParserState.CHECK_ENABLE:
            curr += input[i]
            if curr == "do()":
                enable = True
                state = ParserState.SEARCHING
            elif curr == "don't()":
                enable = False
                state = ParserState.SEARCHING 
        elif state == ParserState.VALIDATE_MUL and enable:
            curr += input[i]
            if curr == 'mul(':
                curr = ''
                state = ParserState.PARSE_VAL1
        elif state == ParserState.PARSE_VAL1:
            if input[i] == ',':
                val1 = int(curr)
                curr = ''
                state = ParserState.PARSE_VAL2
                continue

            curr += input[i]
            if not input[i].isdigit():
                state = ParserState.SEARCHING
            elif len(curr) > 3:
                state = ParserState.SEARCHING
        elif state == ParserState.PARSE_VAL2:
            if input[i] == ')':
                val2 = int(curr)
                sum += val1 * val2
                state = ParserState.SEARCHING
                continue
             
            curr += input[i]
            if not input[i].isdigit():
                state = ParserState.SEARCHING
            elif len(curr) > 3:
                state = ParserState.SEARCHING

    return sum


input_file = 'inputs/day3.txt'

input = ''

with open(input_file) as file:
    input = file.read()
    

print(f'sum of uncorrupted muls = {sum_uncorrupted_muls(input)}')
print(f'sum of enabled uncorrupted muls = {sum_enabled_uncorrupted_muls(input)}')