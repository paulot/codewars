
def f(queens):
  nattacks = [0] * len(queens)
  for row1, col1 in enumerate(queens):
    found_same_col = False
    found_diag_down, found_diag_up = False, False
    for row2, col2 in enumerate(queens[row1+1:], row1+1):
      if col1 == col2 and not found_same_col:
        nattacks[row1] += 1
        nattacks[row2] += 1
        found_same_col = True
      if abs(row1-row2) == abs(col1-col2):
        if col2 > col1 and not found_diag_up:
          nattacks[row1] += 1
          nattacks[row2] += 1
          found_diag_up = True
        elif col2 < col1 and not found_diag_down:
          nattacks[row1] += 1
          nattacks[row2] += 1
          found_diag_down = True
  return reduce(max, nattacks)

print f([3,1,4,2]), 0
print f([2,3,1]), 1
print f([1,1,1,1]), 2
print f([1,2,3,4]), 2
print f([4,3,2,1]), 2
print f([2,2,2,2]), 2
print f([3,3,3,3]), 2




