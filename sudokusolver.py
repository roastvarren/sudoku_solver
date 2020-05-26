grid = [[0,6,9,5,8,0,0,0,7],
        [7,0,5,0,0,0,0,0,0],
        [4,0,0,2,0,0,9,0,0],
        [0,2,3,0,0,0,0,0,0],
        [0,0,1,0,0,0,5,0,0],
        [0,0,0,0,0,0,8,9,0],
        [0,0,4,0,0,5,0,0,9],
        [0,0,0,0,0,0,2,0,5],
        [5,0,0,0,3,4,6,7,0]]

def solve(b):
  find = find_empty(grid)
  if not find:
    return True # if there are no empty squares left, grid is solved
  else:
    row, col = find
  
  for i in range(1, 10):
    if is_valid(b, i, (row, col)):
      b[row][col] = i # if value is valid, insert value

      if solve(b): # call solve() on the new grid
        return True
      
      b[row][col] = 0 # last value is reset if solve() not possible

  return False

def is_valid(b, n, pos):
  for i in range(len(b[0])): # check row
    if b[pos[0]][i] == n and pos[1] != i:
      return False

  for i in range(len(b)): # check column 
    if b[i][pos[1]] == n and pos[0] != i:
      return False

  box_x = pos[1] // 3
  box_y = pos[0] // 3

  for i in range (box_y*3, box_y*3 + 3): # check box
    for j in range (box_x*3, box_x*3 + 3):
      if b[i][j] == n and (i, j) != pos:
        return False

  return True

def print_board(b):
  for i in range(len(b)):
    if i % 3 == 0 and i != 0:
      print('- - - - - - - - - - -')

    for j in range(len(b[0])):
      if j % 3 == 0 and j != 0:
        print('| ', end='')

      if j == 8:
        print(b[i][j])
      else:
        print(str(b[i][j]) + ' ', end='')

def find_empty(b):
  for i in range(len(b)):
    for j in range(len(b[0])):
      if b[i][j] == 0:
        return (i, j) # row, col - use as 'pos' in is_valid function    
  return None

print('Sudoku grid:\n\n')
print_board(grid)
solve(grid)
print('\n\nSolution:\n\n')
print_board(grid)
