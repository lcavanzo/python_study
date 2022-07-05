# Write a program that using the grid, generate the following output
#   ..OO.OO..
#   .OOOOOOO.
#   .OOOOOOO.
#   ..OOOOO..
#   ...OOO...
#   ....O....

grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
]

new_list = []

for index_row,row in enumerate(grid):
    print(index_row)
    for 


