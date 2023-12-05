import numpy as np
import string
import re

with open('day03_input.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

def find_numbers(data):
    numbers = []
    for r, row in enumerate(data):
        matches = re.finditer('\d+', row)
        for m in matches:
            numbers.append((int(m.group()), (r, m.start(), m.end())))
    return numbers
    
def get_neighbors(pos, grid):
    nrow = []
    ncol = []
    nvals = []
    r, c0, c1 = pos
    rmax = grid.shape[0] - 1
    cmax = grid.shape[1]
    if r > 0:
        nrow.extend((c1-c0)*[r-1])
        ncol.extend([x for x in range(c0, c1)])
        if c0 > 0:
            nrow.append(r-1)
            ncol.append(c0-1)
        if c1 < cmax:
            nrow.append(r-1)
            ncol.append(c1)
    if r < rmax:
        nrow.extend((c1-c0)*[r+1])
        ncol.extend([x for x in range(c0, c1)])
        if c0 > 0:
            nrow.append(r+1)
            ncol.append(c0-1)
        if c1 < cmax:
            nrow.append(r+1)
            ncol.append(c1)
    if c0 > 0:
        nrow.append(r)
        ncol.append(c0-1) 
    if c1 < cmax:
        nrow.append(r) 
        ncol.append(c1)         

    nvals = grid[(nrow, ncol)]
    return nrow, ncol, nvals

def is_part(entry, grid):
    num, pos = entry
    no_symbols = set('.')
    _, _, vals = get_neighbors(pos, grid)
    return not (set(vals) == no_symbols)
    
schematic = np.array([list(x) for x in data])

########## Part 1 ########
parts = []
part_nums = []
numbers = find_numbers(data)
for ID, entry in enumerate(numbers):
    if is_part(entry, schematic):
        parts.append(entry)
        part_nums.append(entry[0])
print(f"Sum of parts: {sum(part_nums)}")


########## Part 2 ########
gear_candidates = dict()
for num, p in parts:
    rix, cix, sym = get_neighbors(p, schematic)
    for ix in np.where(sym == '*')[0]:
        astk = (rix[ix], cix[ix])
        if astk in gear_candidates:
            gear_candidates[astk].append(num)
        else:
            gear_candidates[astk] = [num]

gear_ratios = []
for gr in gear_candidates.values():
    if len(gr) == 2:
        gear_ratios.append(gr[0]*gr[1])
print(f"Sum of gear ratios: {sum(gear_ratios)}")