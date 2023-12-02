with open('day02_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

def find_game_maxes(line):
    maxes = [0,0,0]
    ID, play = line.split(':')
    ID = int(ID.split()[1])

    sets = play.split(';')
    for s in sets:
        cubes = s.split(',')
        for c in cubes:
            if 'red' in c:
                i = 0
            elif 'green' in c:
                i = 1
            else:
                i = 2
            val = int(c.split()[0])
            if val > maxes[i]:
                maxes[i] = val
    return ID, maxes

rmax = 12
gmax = 13
bmax = 14

possible_games = []
minimum_set_power = []
for line in data:
    ID, maxes = find_game_maxes(line)
    if rmax >= maxes[0] and gmax >= maxes[1] and bmax >= maxes[2]: ### Part 1
        possible_games.append(ID)

    minimum_set_power.append(maxes[0] * maxes[1] * maxes[2])
print(f'Sum of IDs of possible games: {sum(possible_games)}')
print(f'Sum of the powers of minimal sets: {sum(minimum_set_power)}')

