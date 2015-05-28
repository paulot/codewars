"""
Any live cell with fewer than two live neighbours dies, as if caused by under-population.
Any live cell with two or three live neighbours lives on to the next generation.
Any live cell with more than three live neighbours dies, as if by overcrowding.
Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
"""
def get(cells, i, j):
  try:
    return cells[i][j] if i > -1 and j > -1 else 0
  except IndexError:
    return 0


def num_neighbors(cells, i, j):
  return (get(cells, i, j+1) + get(cells, i, j-1) + get(cells, i+1, j) +
          get(cells, i-1, j) + get(cells, i-1, j-1) + get(cells, i-1, j+1) +
          get(cells, i+1, j-1) + get(cells, i+1, j+1))


def next_cell(cell, i, j):
  n = num_neighbors(cell, i, j)
  return int(0 if n < 2 or n > 3 else 1 if cell[i][j] else n == 3)


def next_gen(cells):
  return [[next_cell(cells, i, j) for j in range(len(cells[i]))] for i in range(len(cells))]

