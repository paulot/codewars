def checkSol(num, sol):
  if num and num in sol:
    del sol[sol.index(num)]

def checkSquare(board, qx, qy, sol):
  qx *= 3
  qy *= 3
  for i in range(qx, qx+3):
    for j in range(qy, qy+3):
      checkSol(board[i][j], sol)

def checkVertical(board, x, sol):
  for i in range(0, 9):
    checkSol(board[x][i], sol)

def checkHorizontal(board, y, sol):
  for i in range(0, 9):
    checkSol(board[i][y], sol)


def getPossible(board, x, y):
  if board[x][y] != 0:
    return [board[x][y]]

  sol = [1,2,3,4,5,6,7,8,9]

  checkSquare(board, x/3, y/3, sol)
  checkVertical(board, x, sol)
  checkHorizontal(board, y, sol)
  return sol

def isSolved(board):
  for line in range(0, 9):
    horizontal = [1,2,3,4,5,6,7,8,9]
    vertical = [1,2,3,4,5,6,7,8,9]
    square = [1,2,3,4,5,6,7,8,9]
    checkHorizontal(board, line, horizontal)
    checkVertical(board, line, vertical)
    checkSquare(board, line%3, line/3, square)
    if horizontal != [] or vertical != [] or square != []:
      return False
  return True

def findOpen(board):
  for i in range(0, 9):
    for j in range(0, 9):
      if board[i][j] == 0:
        return (i, j)

def solve(board):
  if isSolved(board):
    return board

  x, y = findOpen(board)
  for possible in getPossible(board, x, y):
    board[x][y] = possible
    # Traverse down
    solved = solve(board)
    if solved:
      return solved
  board[x][y] = 0
  return None

