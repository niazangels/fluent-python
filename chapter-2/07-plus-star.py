l = [1, 2, 3]
x = l * 5
print(x)

# The generator way to create lists
print('\n\n> Create a tic-tac-toe board')
board = [['_'] * 3 for _ in range(3)]
print(board)
board[1][1] = 'X'
print(board)

# What really happens
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print('What really happens')
print(board)
# Wrong method follows. It returns 3 references instead of copies
print('\n\n> Wrong method')
board = [['_'] * 3] * 3
print(board)
board[1][1] = 'X'
print(board)

# What really happens
row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)
print('What really happens')
print(board)
