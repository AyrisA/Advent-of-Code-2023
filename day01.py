with open('day01_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

##################### Part 1 #####################
calibration_values = []

for line in data:
    for c in line:
        if c.isnumeric():
            digit1 = c
            break
    rline = list(line)
    rline.reverse()
    for c in rline:
        if c.isnumeric():
            digit2 = c
            break
    calibration_values.append(int(digit1 + digit2))

print('Part 1:')
print(f'The sum of all my calibration values is: {sum(calibration_values)}\n')

##################### Part 2 #####################

def find_first_digit(line):
    digits = {'one':'1',
              'two':'2',
              'three':'3',
              'four':'4',
              'five':'5',
              'six':'6',
              'seven':'7',
              'eight':'8',
              'nine':'9'}
    
    segment = ''
    for c in line:
        if c.isnumeric():
            num = c
            break
        else:
            segment += c

    loc = len(line)
    for d in digits:
        if d in segment:
            this_loc = segment.index(d)
            if this_loc < loc:
                loc = this_loc
                num = digits[d]

    return num


def find_last_digit(line):
    digits = {'one':'1',
              'two':'2',
              'three':'3',
              'four':'4',
              'five':'5',
              'six':'6',
              'seven':'7',
              'eight':'8',
              'nine':'9'}
    
    segment = ''
    for c in reversed(line):
        if c.isnumeric():
            num = c
            break
        else:
            segment += c
    segment = ''.join(reversed(segment))

    loc = -1
    for d in digits:
        if d in segment:
            this_loc = segment.rindex(d)
            if this_loc > loc:
                loc = this_loc
                num = digits[d]

    return num

calibration_values = []
for line in data:
    calibration_values.append(int(find_first_digit(line) + find_last_digit(line)))

print('Part 2:')
print(f'The sum of all my calibration values is: {sum(calibration_values)}\n')
